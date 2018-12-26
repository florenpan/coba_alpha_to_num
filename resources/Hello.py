from flask_restful import Resource, reqparse


class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}
    
    def post(self):
        mesin_parse = reqparse.RequestParser()
        mesin_parse.add_argument('angka')
        args = mesin_parse.parse_args()
        print(args)

        if args.angka == 'a':
            return 1
        elif args.angka == 'b':
            return 2
        else:
            return 'udah abis'