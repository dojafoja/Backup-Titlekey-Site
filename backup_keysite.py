import os, shutil, sys, json
from time import sleep
try:
    from urllib import urlretrieve as retrieve
except ImportError:
    from urllib.request import urlretrieve as retrieve


class TicketGrabber:
    def load_titles(self):
        x = []
        try:            
            if sys.version_info[0] == 3:
                with open('titlekeys.json', encoding='utf-8') as td:
                    title_data = json.load(td)
            else:
                with open('titlekeys.json') as td:
                    title_data = json.load(td)
                    
            for i in title_data: 
                if i['name']:
                    titleid = i['titleID']
                    if int(i['ticket']):
                        x.append(titleid)
                    
            return x
        
        except Exception as e:
            print(e)


    def download_titlekeys_file(self):
        print('Downloading titlekeys.json from {}'.format(keysite))
        retrieve('{}/json'.format(keysite),'titlekeys.json')

    
    def find_missing_tickets(self):
        missing = []
        x = []
    
        for tik in os.listdir(os.path.join(os.getcwd(), 'ticket')):
            if tik.endswith('.tik'):
                x.append(tik[:-4])

        for i in self.load_titles():
            if not i in x:
                missing.append(i)
            
        return missing
            
        
    
    def download_missing_tickets(self, missing):
        qty = len(missing)
        print('Missing {} tickets.'.format(qty))
        if missing:
            for i in enumerate(missing, 1):
                titleid = i[1]
                print('Downloading {}:   {} of {}'.format(titleid + '.tik', i[0], qty))
                retrieve('{}/ticket/{}.tik'.format(keysite, titleid), os.path.join('ticket', '{}.tik'.format(titleid)))
    


    def update(self):
        try:
            self.download_titlekeys_file()
            self.download_missing_tickets(self.find_missing_tickets())
            shutil.move('titlekeys.json', os.path.join('json', 'index.html'))
        except IOError:
            print('ERROR: COULD NOT CONNECT TO KEYSITE URL')

        print('Done backing up keysite. Exiting in 5 seconds.........')
        sleep(5)
        sys.exit()
        
        




def get_keysite_url():
    with open('keysite_url.txt', 'r') as f:
        site = f.readline().strip()
    return site

if not os.path.isdir('json'):
    os.mkdir('json')
if not os.path.isdir('ticket'):
    os.mkdir('ticket')

keysite = get_keysite_url()
grabber = TicketGrabber()
grabber.update()




