# China timezone if you are from others please change this
TIME_ZONE = "Asia/Shanghai"

# shanbay -- no need to login
SHANBAY_CALENDAR_API = "https://apiv3.shanbay.com/uc/checkin/calendar/dates/?user_id={user_name}&start_date={start_date}&end_date={end_date}"

# duolingo -- no need to login
DUOLINGO_CALENDAR_API = "https://www.duolingo.com/2017-06-30/users/{user_id}/xp_summaries?endDate={end_date}&startDate={start_date}&timezone=Asia/Shanghai"

# cichang -- need to login
HJ_APPKEY = "45fd17e02003d89bee7f046bb494de13"
CICHANG_LOGIN_URL = "https://pass.hujiang.com/Handler/UCenter.json?action=Login&isapp=true&language=zh_CN&password={password}&timezone=8&user_domain=hj&username={user_name}"
CICHANG_COVERT_URL = "https://pass-cdn.hjapi.com/v1.1/access_token/convert"
CICHANG_CLAENDAR_URL = "https://cichang.hjapi.com/v3/user/center/?userId={user_id}&startDate={start_date}&endDate={end_date}"

# switch -- need to packet sniffer (to get device id and token)
