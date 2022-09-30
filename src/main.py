import ntplib
from time import ctime


if __name__ == '__main__':
    c = ntplib.NTPClient()
    response = c.request('time.google.com')
    print(response.offset)
    ctime(response.tx_time)
