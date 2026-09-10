import sys
import datetime


def log_err(msg):
    log_write('error', msg)


def log_wrn(msg):
    log_write('warning', msg)


def log_inf(msg):
    log_write('info', msg)


def log_dbg(msg):
    log_write('debug', msg)


def log_write(lv, msg):
    cp = get_color_pallete(lv)
    pos = get_call_position()
    print('%s %s' % (cp.c1, get_timestamp()), end=' ')
    print('%s %s' % (cp.c2, lv.upper()), end=' ')
    print('%s %s:%d' % (cp.c3, pos.file, pos.line), end=' ')
    print('%s %s()' % (cp.c4, pos.function), end=' ')
    print('%s %s \x1b[0m' % (cp.c5, msg))


def get_timestamp():
    return datetime.datetime.now().isoformat(sep=' ')


def get_call_position():
    frm = sys._getframe(3)
    pos = CallPosition()
    pos.file = frm.f_code.co_filename
    pos.line = frm.f_lineno
    pos.function = frm.f_code.co_name
    return pos


class CallPosition(object):

    def __init__(self):
        self.file = ''
        self.line = 0
        self.function = ''


def get_color_pallete(lv):
    if lv.lower().strip() in ('error', 'warning'):
        return ColorPalleteForError()
    else:
        return ColorPalleteBase()


class ColorPalleteBase(object):

    def __init__(self):
        self.c1 = '\x1b[48;2;210;210;210;30m'
        self.c2 = '\x1b[48;2;230;230;30;30m'
        self.c3 = self.c1
        self.c4 = self.c2
        self.c5 = '\x1b[106;30m'


class ColorPalleteForError(ColorPalleteBase):

    def __init__(self):
        super().__init__()
        self.c2 = '\x1b[41;30m'
        self.c4 = self.c2
            
