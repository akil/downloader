# -*- coding: utf-8 -*-

import os
import pipes
import cookielib
import tempfile
import subprocess
import logging


_LOG = logging.getLogger(__name__)


def _write_torrent(path, stream):

    with open(path, 'wb') as f:
        for chunk in stream.iter_content(1024):
            f.write(chunk)
    stream.close()

def store(todownload, config):

    url = todownload.results['url']
    if not url.startswith('http://') and not url.startswith('https://'):
        _LOG.error("url:ko addr:%s" % url)
        print "\t[*] Can't store magnet link"
        return

    if config['path'] is None:
        path = "%s.torrent" % tempfile.NamedTemporaryFile().name
    else:
        filename = "%s.torrent" % todownload.results['filename']
        path     = os.path.join(config['path'], filename)

    page = todownload.session.get(url, stream=True, verify=False)

    _write_torrent(path, page)


def cmd(todownload, config):

    url = todownload.results['url']

    _LOG.debug("url: %s" % url)

    if not url.startswith('http://') and not url.startswith('https://'):
        torrent = url
    else:
        torrent = "%s.torrent" % tempfile.NamedTemporaryFile().name
        page    = todownload.session.get(url,
                                         stream=True,
                                         verify=False)
        _write_torrent(torrent, page)

    path = pipes.quote(todownload.vf.path)
    cmd  = (' '.join(config['transmission']) % (torrent, path)).split()

    try:
        r = subprocess.Popen(cmd,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)
    except OSError as e:
        _LOG.error("add:failed cmd:%r error:%s" % (cmd, e.strerror))
    else:
        stdout, stderr = r.communicate()

        if int(r.returncode) != 0:
            _LOG.error("add:failed code:%d cmd:%r error:%s" % (r.returncode, cmd, stdout.replace('\n', ' ')))

    if os.path.isfile(torrent): os.remove(torrent)



def cmd2(todownload, config):

    filepath = os.path.join(config['home'], 'cookies.txt')
    cookie   = cookielib.MozillaCookieJar(filepath)

    for c in todownload.session.cookies: cookie.set_cookie(c)

    try:
        cookie.save()
    except Exception as e:
        _LOG.debug("cookie:ko error:%s" % str(e))
    else:
        os.chmod(filepath, 0777)

        url, path = todownload.results['url'], todownload.vf.path
        cmd = (' '.join(config['transmission']) % (url, path)).split()

        try:
            r = subprocess.Popen(cmd,
                                 stdout = subprocess.PIPE,
                                 stderr = subprocess.PIPE)
        except OSError as e:
            _LOG.error("add:failed cmd:%r error:%s" % (cmd, e.strerror))
        else:
            stdout, stderr = r.communicate()

            if int(r.returncode) != 0:
                _LOG.error("add:failed code:%d cmd:%r error:%s" % (r.returncode, cmd, stdout.replace('\n', ' ')))

        os.remove(filepath)
