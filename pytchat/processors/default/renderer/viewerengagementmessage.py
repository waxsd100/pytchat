from .base import BaseRenderer

AUTHOR_CHANNEL_ID = "000000000000000000000000"
AUTHOR_NAME = "YouTube system message"
AUTHOR_IMAGEURL = "https://yt3.ggpht.com/584JjRp5QMuKbyduM_2k5RlXFqHJtQ0qLIPZpwbUjMJmgzZngHcam5JMuZQxyzGMV5ljwJRl0Q=s64-c-k-c0x00ffffff-no-rj"


class LiveChatViewerEngagementMessageRenderer(BaseRenderer):
    def settype(self):
        if self.item.get("icon", {}).get("iconType") == "POLL":
            self.chat.type = "poll"
        elif self.item.get("icon", {}).get("iconType") == "CELEBRATION":
            self.chat.type = "celebration"
        else:
            self.chat.type = "viewerEngagementMessage"

    def get_authordetails(self):
        self.chat.author.badgeUrl = ""
        (self.chat.author.isVerified,
         self.chat.author.isChatOwner,
         self.chat.author.isChatSponsor,
         self.chat.author.isChatModerator) = (
            self.get_badges(self.item)
        )
        self.chat.author.channelId = AUTHOR_CHANNEL_ID
        self.chat.author.channelUrl = "http://www.youtube.com/"
        self.chat.author.name = AUTHOR_NAME
        self.chat.author.imageUrl = AUTHOR_IMAGEURL
