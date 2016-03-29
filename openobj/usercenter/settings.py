# 注册邮件模板
REG_EMAIL_SUBJECT = 'OpenObj邮箱验证'
REG_EMAIL_CONTENT_TEMPLATE = """
        <table cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td bgcolor="#edf1e3" width="100%" style="padding: 40px;">
                    <table cellspacing="0" cellpadding="0" style="margin: 0 auto;font-family: 'Microsoft Yahei',arial,sans-serif;border-collapse:collapse">
                        <tr>
                            <td width="300px" height="50px"><img src="https://passport.wiwide.com/static/images/wiwide-logoemail.jpg" alt="" /></td>
                            <td width="300px" style="text-align: right;vertical-align: bottom;padding-bottom: 5px;">邮箱验证</td>
                        </tr>
                        <tr>
                            <td colspan="2" height="10px" style="background: #e68781 url(https://passport.wiwide.com/static/images/wiwide_gapemail.jpg) no-repeat;"></td>
                        </tr>
                        <tr>
                            <td colspan="2" height="340px" width="600px" bgcolor="#fff" style="border: 1px solid #ddd;border-top: 0;border-bottom: 0">
                                <div style="padding: 25px 55px;">
                                    <p style="margin: 0 0 25px 0;">亲爱的 {username}，您好！</p>
                                    <p>点击下面的链接即可激活账号并绑定邮箱</p>
                                    <p style="margin: 0 0 25px 0;"><a href="{url}" style="color: #1b77ff;">{url}</a></p>
                                    <p style="margin: 25px 0; line-height: 1.5em;">为了确保您的账号安全，该链接仅24小时内访问有效。如果以上连接无法点击，请复制链接到浏览器中打开。</p>
                                    <p style="margin: 0; padding: 15px 0 0 0;">请勿直接回复邮件！</p>
                                    <p style="margin: 5px 0 0 0; padding: 0;">OpenObj</p>
                                    <p style="margin: 5px 0 0 0; padding: 0;">{date_now}</p>
                                </div>
                            </td>
                        </tr>
                         <tr>
                            <td colspan="2" height="10px" style="background: #e68781 url(https://passport.wiwide.com/static/images/wiwide_gapemail.jpg) no-repeat;"></td>
                        </tr>
                        <tr><td colspan="2"><p style="text-align: center;color: #828284; font-size: .8em;">Copyright?2007-2014 WiWide Inc 迈外迪科技 沪ICP备08023648</p></td></tr>
                    </table>
                </td>
            </tr>
        </table>
    """
