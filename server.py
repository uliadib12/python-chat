import asyncio
import websockets

async def handle_connection(websocket, path):
    # Menerima pesan dari klien
    async for message in websocket:
        print(f"Received message: {message}")

        # Memproses pesan (sesuai kebutuhan Anda)
        response = f"You said: {message}"

        # Mengirim balasan ke klien
        await websocket.send(response)
        print(f"Sent message: {response}")

# Menjalankan WebSocket server
start_server = websockets.serve(handle_connection, 'localhost', 12345)

async def main():
    async with start_server:
        print("WebSocket server started...")
        await asyncio.Future()  # Memblokir eksekusi agar server berjalan terus

asyncio.run(main())
