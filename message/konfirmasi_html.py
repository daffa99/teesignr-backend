message = '''
<table style="background-color:#fff;margin:5% auto;width:100%;max-width:600px" cellspacing="0" cellpadding="0" border="0" bgcolor="#fff" align="center">

	<tbody><tr>
		<td>
			<table style="padding:10px 15px;font-size:14px" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#F96C00" align="center">
				<tbody><tr>
					<td style="padding:5px 0 0" width="60%" align="center">
						<span style="font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:#fff">ORDER INFORMATION (TEESIGNR)</span>
					</td>
				</tr>
			</tbody></table>
		</td>
	</tr>
	<tr>
		<td style="padding:25px 15px 10px">
			<table width="100%">
				<tbody><tr>
					<td width="100%">
						<h1 style="font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;margin:0;font-size:16px;font-weight:bold;line-height:24px;color:rgba(0,0,0,0.70)">Hello {},</h1>
					</td>
				</tr>
				<tr>
					<td width="100%">
						<p style="font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;margin:0;font-size:16px;line-height:24px;color:rgba(0,0,0,0.70)">Thank you for purchasing our T-Shirt(s)!<br>
                            You are successfully help one of our designer by buying their product(s). Now, you just need to wait for the T-Shirt(s) to come into specified address. Don't forget to prepare your ca$$h. To remind you, so here it is your order details: <br></p>
					</td>
                </tr>
                </tbody>
            </table>
        </td>
    </tr>
<table style="margin:15px 0;color:rgba(0,0,0,0.70);font-size:14px;border-collapse:collapse" width="100%">
    <tbody>
        <tr>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0" width="40%">Nomor Pemesanan</td>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0;font-weight:bold" width="60%">{}</td>
        </tr>
        <tr>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0" width="40%">Total Harga</td>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0;font-weight:bold" width="60%">{}</td>
            </tr>
        <tr>
        <tr>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0" width="40%">Metode Pembayaran</td>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0;font-weight:bold" width="60%">{}</td>
            </tr>
        <tr>
        <tr>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0" width="40%">Nama Penerima</td>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0;font-weight:bold" width="60%">{}</td>
            </tr>
        <tr>
        <tr>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0" width="40%">Nomor Telepon</td>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0;font-weight:bold" width="60%">{}</td>
            </tr>
        <tr>
        <tr>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0" width="40%">Alamat Penerima</td>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0;font-weight:bold" width="60%">{}</td>
            </tr>
        <tr>
        <tr>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0" width="40%">Detail Pesanan</td>
            <td style="border-top:1px solid rgba(0,0,0,0.12);border-bottom:1px solid rgba(0,0,0,0.12);padding:10px 0;font-weight:bold" width="60%">{}</td>
            </tr>
        <tr>
            <td>
                <h1 style="font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;margin:0;font-size:16px;font-weight:bold;line-height:24px;color:rgba(0,0,0,0.70)">Happy Teesigning!</h1>
            </td>
        </tr>
    </tbody>
</table>
</tbody></table>
'''
def PesananEmail(full_name, pesanan_id, total_harga, metode_pembayaran, nama_penerima, nomor_telepon, alamat_penerima, daftar_belanjaan):
    format_pesanan = "{}, Qty: {}, Size: {} <br>"
    daftar_pesanan = ""
    for barang in daftar_belanjaan:
        detail_pesanan = format_pesanan.format(barang['nama_barang'], barang['jumlah'], barang['ukuran'])
        daftar_pesanan += detail_pesanan
    return message.format(full_name, pesanan_id, total_harga, metode_pembayaran, nama_penerima, nomor_telepon, 
    alamat_penerima, daftar_pesanan)