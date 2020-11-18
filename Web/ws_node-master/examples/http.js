let http = require('http');
let server = http.createServer(
    function (request, response) {
        // respond to the request
        response.setHeader("Content-Type", "text/plain");
        response.end('Hello World at ' + request.url + '\n');
    }
);
server.listen(8080);  // node never stops, mostly waits
