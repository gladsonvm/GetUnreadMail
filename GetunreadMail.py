import imaplib
import email
def GetUnreadMail():

    conn = imaplib.IMAP4(raw_input("imapserver:\n"))#replace IMAP4 with IMAP_SSL for secured sites
    conn.login(raw_input("usrname:\n"),raw_input("password:\n"))
    conn.list()
    conn.select('INBOX')
    unreadflag,unreadlist = conn.search(None,'(UNSEEN)')
    # from_name=from_addr=body = ''
    if unreadflag == 'OK':
      for message in unreadlist[0].split():
          stat,data = conn.fetch(message,'(RFC822)')
          msg = HeaderParser().parsestr(data[0][1])
          from_name = email.utils.parseaddr(msg['From'])[0]
          from_addr = email.utils.parseaddr(msg['From'])[1]
          Subject = msg['Subject']
          mail = email.message_from_string(data[0][1])
          payload=''
          for part in mail.walk():
            if part.get_content_subtype()=='plain':
                payload = part.get_payload()
          body = payload.strip('\r\n')
    print ('from:%s\n email:%s\n content:%s\n') %(from_name,from_addr,body)

GetUnreadMail()