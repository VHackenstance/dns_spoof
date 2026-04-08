<h3>DNS SPOOF</h3>
<h4>Dunno...</h4>
<p>
<b>DNS (Domain Name System):</b> Hierarchical, distributed service that translates human-readable domain names (like www.example.com) into machine-readable IP addresses (like 192.0.2.44) required to locate devices on the internet.
</p>
<p>
Often described as the <b>phonebook of the internet</b>, it has been an essential component of internet functionality since November 1983.
</p>
<p>So, what ARP does for MAC and IP Addresses, DNS does for Domain Names and IP Addresses.</p>
<p>
<b>DNS spoofing:</b> Also known as DNS cache poisoning, is a cyberattack where an attacker corrupts a DNS resolver's cache with false data to redirect users from legitimate websites to fraudulent ones. 
</p>
<p>
This manipulation causes the name server to return an incorrect IP address, tricking users into visiting fake sites that often mimic the original destination to steal sensitive information like login credentials or financial data.
</p>


<h3>Setup testing on our local computer.</h3>
<h4>Process:</h4>
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
<h4>Finally found active http site for testing:</h4>
<p><b>http://testasp.vulnweb.com/</b></p>
<p>Login:</p>
<p>Username: <b>admin</b></p>
<p>Password: <b>none</b></p>
<h4>Remove the IP Table Rules.</h4>
<p>When we are done testing be sure to remove the ip table rules.</p>
<p><b>iptables --flush</b></p>
<p>You can confirm the iptables flush by running</p>
<p><b>sudo iptables -L -n</b></p>
<p>And there will be zero rules under the chains (headings)</p>