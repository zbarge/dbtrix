############################################################################
##
## Copyright (C) 2014 Moritz Warning <moritzwarning@web.de>.
## Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
## Contact: Nokia Corporation (qt-info@nokia.com)
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
############################################################################


from zeex.core.compat import QtNetwork
from zeex.ext.ftp.ftpreply import FtpReply


class NetworkAccessManager(QtNetwork.QNetworkAccessManager):

    def __init__(self, manager, parent):
        super(NetworkAccessManager, self).__init__(parent)

        self.setCache(manager.cache())
        self.setCookieJar(manager.cookieJar())
        self.setProxy(manager.proxy())
        self.setProxyFactory(manager.proxyFactory())

    def createRequest(self, operation, request, device):
        if request.url().scheme() != "ftp":
            return QtNetwork.QNetworkAccessManager.createRequest(self, operation, request, device)

        if operation == QtNetwork.QNetworkAccessManager.GetOperation:
            # Handle ftp:// URLs separately by creating custom QNetworkReply objects.
            return FtpReply(request.url(), self)
        else:
            return QtNetwork.QNetworkAccessManager.createRequest(self, operation, request, device)
