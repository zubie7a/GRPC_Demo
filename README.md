## Santiago Zubieta
#### 2016

## GRPC Demo

Demo app sent messages from cellphones visiting a website, and then retrieved from a **Raspberry Pi** with the **SenseHAT**'s LED matrix, displaying information _(and a Gopher!)_
[![][01]](https://www.youtube.com/watch?v=DSW_CQc_Wi4)


**:8080** is the port for the Web Server.  
**:50001** is the port for the GRPC Server.  
```
$ go get -u github.com/zubie7a/GRPC_Demo
$ go run $GOPATH/src/github.com/zubie7a/GRPC_Demo
```

[01]: https://i.imgur.com/WS1A46r.png "GRPC Demo"