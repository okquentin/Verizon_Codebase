const net = require('net');
const port = 21;

let carPosition;
let carSpeed;

// Create a server object
const server = net.createServer((socket) => {
    
    socket.on('data', (data) => {
        // Parse JSON string to JSON object
        const jsonData = JSON.parse(data.toString());

        // Log the data
        console.log(jsonData);
    
        carPosition = jsonData.carX;
        humanPosition = jsonData.pedestrianY;
    });

    try{
    if(humanPosition != null && carPosition != null){
        if(humanPosition > 0 && humanPosition < 7){
            carSpeed = 0;
        } 
    }
    }
    catch{console.log("Cant stop car");}
});

// Define the port on which you want to connect

// Listen for connections on the specified port
server.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
