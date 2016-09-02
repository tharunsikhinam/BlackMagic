/**
 * Created by quikr on 8/30/16.
 */

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);


io.on('connection', function(socket){
     console.log('a user connected');
});

http.listen(3000, function(){
    console.log('listening on *:3000');
});
