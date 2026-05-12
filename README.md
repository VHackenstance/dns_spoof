<h3>UPDATE: Works but you have to be very specific with the DNS</h3>
<p>Works with www.pentest-standard.org, not http://www.pentest-standard.org/index.php/Main_Page</p>
<p>Works with </p>
<h3>DNS SPOOF</h3>
<h4>Intercepting and Modifying Packets</h4>
<h4>Serve an IP to a target when they request another specific target</h4>

<p>We setup our classic onPath with arp spoof.</p>

<h3>Setup testing on our local computer.</h3>
<h4>Start the local web server</h4>
<p><b>sudo systemctl start apache2</b>: 
Then enter your IP into the browser.
<br />
This file the index.html is accessible at <b>/var/www/html/</b>

</p>
<h4>Process:</h4>
    <h4>Remove the IP Table Rules.</h4>
    <p><b>iptables --flush</b></p>
    <p>Confirm iptables flushed: <b>sudo iptables -L -n</b></p>
    <h4>scapy.DNSRR</h4>
    <p>Look for the <b>qd</b>DNS Question Recorder (QR). <br/> 
We are interested in <b>qtype = A</b>, which assigns the Domain Name to the IP.
Which should have one or more answers <b>an</b>: DNS Question Record.  
<b>Type = A</b> <br/>
We want to modify the field <b>rdata = [IP Address]</b> with our IP Address.
</p>
<p>So we want to check if the user is going to the target website.</p>
    <p>Run script: <b>sudo python dns_spoof.py</b> in one terminal window.</p>
    <p>Run ping: <b>ping -c 1 www.bing.com, </b>in another window.  You should get the following with your IP</p>
    ![ping_screen_shot.png](assets/ping_screen_shot.png)
    <p>So, the target has requested to go to bing.com, but the 
    IP we have returned is a spoofed IP and will take it somewhere else.</p>
<h4>Kali Linux create webserver and your own index page on your IP</h4>
<p>When the user tries to navigate to www.bing.com they will be taken to our local page.</p>
<h3>To Test on a Remote VM.</h3>
<ol>
    <li>
        Create, in the terminal, an <b>OUTPUT</b> queue with a value of 0.
<p><b>sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0 --queue-bypass
</b></p>
    </li>
  <li>
        Create an <b>INPUT</b> queue with a value of 0.
<p>These are packets coming into your computer.</p>
<p><b>sudo iptables -I INPUT -j NFQUEUE --queue-num 0 --queue-bypass
</b></p>
    </li>
</ol>
<h4>Set the iptables using our script set_iptables.py</h4>
<ol>
<li>To test locally
<p>sudo python utilities/set_iptables.py -s TRUE -n 0</p>
</li>
<li>To test against a remote location
<p>sudo python utilities/set_iptables.py -r TRUE -n 0</p>
</li>
<li>To flush the iptables
<p>sudo python utilities/set_iptables.py -f TRUE</p>
</li>
</ol>
<h4>Finally found active http sites for testing:</h4>
These sites are ideal as they have a login, account creation, to practise capturing login credentials.
<ul>
    <li>
        <b>http://testasp.vulnweb.com/</b>
        <p>Login Details: Username: <b>admin</b>.  Password: <b>none</b></p>
    </li>
    <li>
        <b>http://testasp.vulnweb.com/</b>
        <p>Login Details: Username: <b>admin</b>.  Password: <b>none</b></p>
    </li>
    <li></li>
</ul>
<p></p>

<h4>Testing a http only site with WebGoat</h4>
    <p>I have created an early testing build file, to use this:</p>
    <p>I installed without an issue using Docker, after installing Docker hehe.</p>
    <p>https://owasp.org/www-project-webgoat/</p>
    <p>Use port lo as this is a loop back.</p>
    <p>Run WebGoat:</p>
    <p>sudo docker run -p 8080:8080 webgoat/webgoat</p>
    <p>Seems to be working so far.</p>
<h4>Arp_spoof + Packet_sniffer</h4>
<ol>

<h4>Scapy can be used to</p>
<ul>
<li>Create Packets</li>
<li>Analyze Packets</li>
<li>Send and Receive Packets</li>
</ul>
<h4>But it cannot be used to <b>Intercept</b> packets/flows</h4>

<h4>We will only run http.  The issues with HTTPS are as follows:</h4>
<ol>
<li><b>Valid SSL Certificate</b>:</li>
<li><b>HSTS Bypass</b>: </li>
<li><b>Traffic Redirection</b>: </li>
</ol>

<h4>Let's run through the basics again.</h4>
<p>
<b>DNS (Domain Name System):</b> Hierarchical, distributed service that translates 
human-readable domain names (like www.example.com) into machine-readable 
IP addresses (like 192.0.2.44) required to locate devices on the internet.
Often described as the <b>phonebook of the internet</b>, it has been an 
essential component of internet functionality since November 1983.
</p>
<p>So, what ARP does for MAC and IP Addresses, DNS does for Domain Names and IP Addresses.</p>
<p>
<b>DNS spoofing:</b> cyberattack where an attacker corrupts a DNS resolver's cache with false data to redirect users from legitimate websites to fraudulent ones. 
</p>
<p>
This manipulation causes the name server to return an incorrect IP address, 
tricking users into visiting fake sites that often mimic the 
original destination to steal sensitive information like 
login credentials or financial details.
</p>
<h3>ISSUES:</h3>
<p>If you get an error message similar to:<br/>
File "netfilterqueue/_impl.pyx", line 282, in netfilterqueue._impl.NetfilterQueue.bind
OSError: Failed to create queue 0.
</p>
<p>$:  ps aux | grep python  </p>
<p></p>

