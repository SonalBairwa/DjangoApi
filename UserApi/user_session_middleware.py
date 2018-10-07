import datetime
import traceback


class UserSessionMiddleware(object):
    @staticmethod
    def process_request(data, request):
        request.session['session_email'] = data.email
        request.session['session_ts'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        request.session['session_user_type'] = data.type
        request.session.modified = True
        return request

    @staticmethod
    def check_session_validation(request):
        session_exp_time = 30 * 60
        try:
            if not request.session.get('session_ts', None):
                return False
            login_ts = datetime.datetime.strptime(request.session.get('session_ts'), '%Y-%m-%d %H:%M:%S')
            session_time = (datetime.datetime.now() - login_ts).seconds
            if session_exp_time <= session_time:
                return False
            else:
                return True

        except Exception as err:
            traceback.print_tb(err.__traceback__)
            return False
