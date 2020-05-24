import asyncio
import ssl


async def echo_client(data, loop):
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_ctx.options |= ssl.OP_NO_TLSv1
    ssl_ctx.options |= ssl.OP_NO_TLSv1_1
    ssl_ctx.load_default_certs()
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.VerifyMode.CERT_REQUIRED
    ssl_ctx.set_ciphers('ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384')
    reader, writer = await asyncio.open_connection('127.0.0.1', 8080, ssl=ssl_ctx, loop=loop)
    print('Sending: {}'.format(data))
    writer.write(len(data).to_bytes(4, byteorder='big'))
    writer.write(data.encode())
    await writer.drain()
    size_bytes = await reader.readexactly(4)
    size = int.from_bytes(size_bytes, byteorder='big')
    echo_data = await reader.readexactly(size)
    print('Received: {}'.format(echo_data))
    writer.close()

if __name__ == '__main__':
    async_loop = asyncio.get_event_loop()
    send_data = "Ping!!!"
    async_loop.run_until_complete(echo_client(send_data, async_loop))
    async_loop.close()
