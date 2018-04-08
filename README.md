## Santiago Zubieta
#### 2016

*'Show me how you do that trick,*  
*"the one that makes me scream" she said*  
*"The one that makes me laugh" she said'*  
-The Cure, Just Like Heaven

## GRPC Demo

Demo app sent messages from cellphones visiting a website, and then retrieved from a Raspberry Pi with SenseHAT, displaying information (and a Gopher!)  
[![](https://github.com/zubie7a/GRPC_Demo/blob/master/static/video.png?raw=true)](https://www.youtube.com/watch?v=DSW_CQc_Wi4)


**:8080** is the port for the Web Server.  
**:50001** is the port for the GRPC Server.  
```
$ go get -u github.com/zubie7a/GRPC_Demo
$ go run $GOPATH/src/github.com/zubie7a/GRPC_Demo
```
