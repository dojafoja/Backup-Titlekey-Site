# Backup-Titlekey-Site

A Python tool to backup and self-host the Titlekey site that is used by NUS downloaders.

This will create the proper folder structure, then connect to the titlekey site url and download everything necessary for a fully working backup. Once backed up you can self-host your own titlekey site using the included server.py file. The server will show you the exact IP address where it is being hosted and you can point NUS downloaders like FunKiiU and FunKii-UI to this IP address. It will behave just like you are using the online titlekey site. The entire thing only uses less than 4 Mb of disk space and includes everything you need to self-host.

Usage:

To backup the titlekey site:
 1. Download and extract all files into a folder
 2. Open the file called keysite_url.txt and enter the URL to the titlekey site. Save file.
 3. Run backup_keysite.py and wait for it to finish.
 4. You can periodically run backup_keysite.py and it will check your backup against the online site and update itself.

To self-host your backed up titlekey site:
 1. Run the included server.py file. You are now self-hosting!
 2. Look at the server window and you will see your IP address.
 2. Point FunKiiU or FunKii-UI to your IP address EXACTLY as it is shown in the server window.

This is tested with FunKii-UI but in theory it should work for any NUS downloader. As long as you can point the downloader to your IP address, either directly in the program or by modifying your hosts file, I imagine it would work fine but hasn't been tested on anything but FunKii-UI

