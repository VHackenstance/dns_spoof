<h3>DNS SPOOF</h3>
<h4>Dunno...</h4>

<h3>Setup testing on our local computer.</h3>
<h4>Process:</h4>
<ol>
    <li>
        Create, in the terminal, an <b>OUTPUT</b> queue with a value of 0.
            <p><b>sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0</b></p>
    </li>
  <li>
        Create an <b>INPUT</b> queue with a value of 0.
            <p>These are packets coming into your computer.</p>
            <p><b>sudo iptables -I INPUT -j NFQUEUE --queue-num 0</b></p>
    </li>
</ol>
<h4>Finally found active http site for testing:</h4>
<p><b>http://testasp.vulnweb.com/</b></p>
<p>Login:</p>
<p>Username: <b>admin</b></p>
<p>Password: <b>none</b></p>