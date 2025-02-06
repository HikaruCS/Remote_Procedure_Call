import json
import os
import math
import socket

class Function :
    @staticmethod
    def floor(x):
        return math.floor(x)

    @staticmethod
    def nroot(n, x):
        return math.floor(x ** (1/n))

    @staticmethod
    def reverse(s):
        return s[::-1]

    @staticmethod
    def validAnagram(s1, s2):
        return sorted(s1) == sorted(s2)

    @staticmethod
    def sort(strArr):
        return sorted(strArr)

    # JSONで送られるデータは文字列だから、関数を実行できるように型を変換する
    def changeType(method, params):
        if method == 'floor':
            return [float(params)]
        elif method == 'nroot':
            param_list = params.split(', ')
            n = int(param_list[0].strip())
            x = float(param_list[1].strip())
            return (n, x)
        elif method == 'reverse':
            return [str(params)]
        elif method == 'validAnagram':
            param_list = params.split(', ')
            return (param_list[0], param_list[1])
        elif method == 'sort':
            return [params.split(', ')]
        else:
            return params

def main():

    functionHashmap = {
        'floor': Function.floor,
        'nroot': Function.nroot,
        'reverse': Function.reverse,
        'validAnagram': Function.validAnagram,
        'sort': Function.sort
    }

    # ソケットを作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # サーバのアドレス
    server_address = '/tmp/json_rpc_socket.sock'
    
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('Starting up on {}'.format(server_address))

    sock.bind(server_address)

    sock.listen(1)

    while True: 
        try:
            while True:
                # クライアントからの接続を受け入れる
                connection, client_address = sock.accept()
                print('---------------')
                print('connection from', client_address)

                # データを最大1024バイト受け取る
                data = connection.recv(1024)

                # 受け取ったデータをデコード
                data_str = data.decode('utf-8')

                # JSON形式のデータをPythonの辞書型に変換
                receivedData = json.loads(data)

                # 受け取ったデータからmethod, params, idを取得
                method = receivedData["method"]
                params = receivedData["params"]
                id = receivedData["id"]

                # 文字列から適切な型へ変換
                params = Function.changeType(method, params)

                if method in functionHashmap:
                    result = functionHashmap[method](*params)
                    
                    answer = {
                        "results": result,
                        "result_type": str(type(result)),
                        "id": id
                    }

                else:
                    answer = {
                        "results": "invalid method",
                        "id": id
                    }

                if data:
                    connection.send(json.dumps(answer).encode('utf-8'))
                    print('answer data: {}'.format(answer))
                else:
                    print('no data from', client_address)
                    break


        finally:
            print('Closing current connection')
            connection.close()

if __name__ == "__main__":
    main()