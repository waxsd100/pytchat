from .base import BaseRenderer


class LiveChatMembershipItemRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "sponsor"

    def get_authordetails(self):
        super().get_authordetails()
        self.chat.author.isChatSponsor = True

    def get_message(self, item):
        try:
            message = ''.join([mes.get("text", "")
                           for mes in item["headerSubtext"]["runs"]])
            self.chat.type = "newSponsor"
            return message, [message]
        except KeyError:
            milestone_text = ''.join([mes.get("text", "")
                           for mes in item["headerPrimaryText"]["runs"]])
            milestone_text = "[" + milestone_text + " " + item["headerSubtext"]["simpleText"] + "]"

            message = ''
            message_ex = []
            runs = item.get("message", {}).get("runs", {})
            for r in runs:
                if not hasattr(r, "get"):
                    continue
                if r.get('emoji'):
                    message += r['emoji'].get('shortcuts', [''])[0]
                    message_ex.append({
                        'id': r['emoji'].get('emojiId').split('/')[-1],
                        'txt': r['emoji'].get('shortcuts', [''])[0],
                        'url': r['emoji']['image']['thumbnails'][0].get('url')
                    })
                else:
                    message += r.get('text', '')
                    message_ex.append(r.get('text', ''))

            if message:
                message = ' '.join([milestone_text, message])
            else:
                message = milestone_text
            if message_ex:
                message_ex[0] = ' '.join([milestone_text, message_ex[0]])
            else:
                message_ex = [milestone_text]
            return message, message_ex
