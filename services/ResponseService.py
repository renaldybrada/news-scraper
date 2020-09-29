class ResponseService:
    def successResponse(self, data):
        response = {
            'status': 'success',
            'code': 200,
            'data': data
        }
        return response, 200

    def errorResponse(self, message, code):
        response = {
            'status': 'error',
            'code': code,
            'message': message,
        }
        return response, code