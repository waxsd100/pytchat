from .base import BaseRenderer


class LiveChatSponsorshipsGiftPurchaseAnnouncementRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "giftPurchase"

    def get_authordetails(self):
        self.chat.author.badgeUrl = ""
        (self.chat.author.isVerified,
         self.chat.author.isChatOwner,
         self.chat.author.isChatSponsor,
         self.chat.author.isChatModerator) = (
            self.get_badges(self.item["header"]["liveChatSponsorshipsHeaderRenderer"])
        )
        self.chat.author.channelId = self.item.get("authorExternalChannelId")
        self.chat.author.channelUrl = "http://www.youtube.com/channel/" + self.chat.author.channelId
        self.chat.author.name = self.item["header"]["liveChatSponsorshipsHeaderRenderer"]["authorName"]["simpleText"]
        self.chat.author.imageUrl = self.item["header"]["liveChatSponsorshipsHeaderRenderer"]["authorPhoto"]["thumbnails"][1]["url"]
        self.chat.author.isChatSponsor = True

    def get_message(self, item):
        message = ''.join([mes.get("text", "")
                       for mes in item["header"]["liveChatSponsorshipsHeaderRenderer"]["primaryText"]["runs"]])
        return message, [message]
