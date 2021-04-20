var app = require("express")();
var http = require("http");
var server = http.Server(app);
var io = require("socket.io")(server);
var port = process.env.PORT || 3000;
const botURL = "http://127.0.0.1:5000/response/";

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

getBotResponse = (msg) => {
  const url = botURL + msg;
  http
    .get(url, (response) => {
      let data = "";
      response.on("data", (chunk) => {
        data += chunk;
      });

      response.on("end", () => {
        io.emit("chat message", data);
      });
    })
    .on("error", (err) => {
      console.log("Error: " + err.message);
    });
};

io.on("connection", function (socket) {
  socket.on("chat message", function (msg) {
    io.emit("chat message", msg);
    getBotResponse(msg);
  });
});

server.listen(port, function () {
  console.log("listening on *:" + port);
});
