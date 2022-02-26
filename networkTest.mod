MODULE Module1
    !***********************************************************
    !
    ! Module:  Module1
    !
    ! Description:
    !   <Insert description here>
    !
    ! Author: love2
    !
    ! Version: 1.0
    !
    !***********************************************************


    !***********************************************************
    !
    ! Procedure main
    !
    !   This is the entry point of your program
    !
    !***********************************************************
    VAR socketdev server;
    VAR socketdev client;
    VAR string msg;
    VAR rawbytes data;
    VAR string clientIP;

    PROC main()
        SocketCreate server;
        SocketBind server,"127.0.0.1",50001;
        SocketListen server;
        SocketAccept server,client\ClientAddress:=clientIP;
        !Sending messages to the client
        SocketSend client,\Str:="Connected, you are: " + clientIP;

        !Getting a message

        SocketReceive client,\RawData:=data;
        UnpackRawBytes data,1,msg\ASCII:=15;
        TPWrite msg;
        SocketSend client,\Str:=msg + " " + clientIP;
        !Closing comms
        SocketClose client;
        SocketClose server;
        
        ERROR
            IF ERRNO=ERR_SOCK_TIMEOUT THEN
                RETRY;
            ELSEIF ERRNO=ERR_SOCK_CLOSED THEN
                server_recover;
                RETRY;
            ELSE
                ! No error recovery handling
            ENDIF
    ENDPROC
    
    PROC server_recover()
    SocketClose server;
    SocketClose client;
    SocketCreate server;
    SocketBind server, "127.0.0.1", 50001;
    SocketListen server;
    SocketAccept server, client\ClientAddress:=clientIP;
    ERROR
        IF ERRNO=ERR_SOCK_TIMEOUT THEN
            RETRY;
        ELSEIF ERRNO=ERR_SOCK_CLOSED THEN
            RETURN;
        ELSE
            ! No error recovery handling
        ENDIF
    ENDPROC

ENDMODULE