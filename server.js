const net = require('net');
const port = 21;

// Create a server object
const server = net.createServer((socket) => {
    socket.on('data', (data) => {
        // Parse JSON string to JSON object
        const jsonData = JSON.parse(data.toString());

        // Log the data
        console.log(jsonData);
    });
});

// Define the port on which you want to connect

// Listen for connections on the specified port
server.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
