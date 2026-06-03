<h3>All scripts are tested and written in and for Linux</h3>
<h3>DNS SPOOF</h3>
<h4>Intercepting and Modifying Packets</h4>
<h4>Serve an IP to a target when they request another specific target</h4>
<p>1. Run arp_spoof for remote testing only.</p>
<p>2. Check ping and webserver access between VMs</p>
<p>3. Port forwarding must be enabled for remote testing.<br/>
<b>echo 1 | sudo tee "/proc/sys/net/ipv4/ip_forward"</b>
<br/>It does not matter for local testing</p>
<p>3. Intercept packets from a Target, place them in our queue.
If we do not forward packets to the Target, the Target
will not have any internet connection. <br />
<b>Packet.accept()</b> will allow the packets to reach the Target.
</p>

<h3>Setup testing on our local computer.</h3>
<h4>Start the local web server</h4>
<p><b>sudo systemctl start apache2</b>: 
Then enter your IP into the browser.
<br />
index.html is accessible at <b>/var/www/html/</b>

</p>
<ol>
    <li>
        Create, in the terminal, an <b>OUTPUT</b> queue with a value of 0.
        <p><b>sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0 --queue-bypass</b></p>
    </li>
  <li>
    Create an <b>INPUT</b> queue with a value of 0.
    <p><b>sudo iptables -I INPUT -j NFQUEUE --queue-num 0 --queue-bypass</b></p>
    </li>
</ol>

<h4>Set the iptables using script set_iptables.py</h4>
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
<h4>Active http sites for testing:</h4>
<ul>
    <li>
        <b>http://testasp.vulnweb.com/</b>
        <p>Login Details: Username: <b>admin</b>.  Password: <b>none</b></p>
    </li>
    <li>
        <b>http://juice-shop.herokuapp.com</b>
        <br/> A caveat here, this is broken a lot of the time.
        <p>Login Details: Username: <b>admin</b>.  Password: <b>none</b></p>
    </li>
</ul>
<p></p>

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
<h3>UPDATE: Works but you have to be specific with the DN</h3>
<p>eg, Works with www.pentest-standard.org, not http://www.pentest-standard.org/index.php/Main_Page</p>

