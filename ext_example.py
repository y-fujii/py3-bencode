import bencode
import datetime


def encode_ext( obj, encode_ext ):
	if isinstance( obj, str ):
		return bencode.encode( obj.encode( "utf-8" ) )
	elif isinstance( obj, datetime.date ):
		return bencode.encode( obj.toordinal() )
	else:
		return bencode.encode( obj, encode_ext )


def decode_ext( buf, i, decode_ext ):
	if b'0'[0] <= buf[i] and buf[i] <= b'9'[0]:
		(text, i) = bencode.decode( buf, i, decode_ext )
		return (text.decode( "utf-8" ), i)
	else:
		return bencode.decode( buf, i, decode_ext )
