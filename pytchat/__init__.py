"""
pytchat is a lightweight python library to browse youtube livechat without Selenium or BeautifulSoup.
"""
__copyright__    = 'Copyright (C) 2019, 2020, 2021 taizan-hokuto'
__version__      = '0.5.6'
__license__      = 'MIT'
__author__       = 'Aiagate'
__author_email__ = '50893541+Aiagate@users.noreply.github.com'
__url__          = 'https://github.com/Aiagate/pytchat'


from .exceptions import (
    ChatParseException,
    ResponseContextError,
    NoContents,
    NoContinuation,
    IllegalFunctionCall,
    InvalidVideoIdException,
    UnknownConnectionError,
    RetryExceedMaxCount,
    ChatDataFinished,
    ReceivedUnknownContinuation,
    FailedExtractContinuation,
    VideoInfoParseError,
    PatternUnmatchError
)

from .api import (
    config,
    LiveChat,
    LiveChatAsync,
    ChatProcessor,
    CompatibleProcessor,
    DummyProcessor,
    DefaultProcessor,
    HTMLArchiver,
    TSVArchiver,
    JsonfileArchiver,
    SimpleDisplayProcessor,
    SpeedCalculator,
    SuperchatCalculator,
    create
)
# flake8: noqa