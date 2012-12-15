import collections


def _decode( x, i, decode ):
	if x[i] == b'i'[0]:
		i += 1
		j = x.index( b'e', i )
		n = int( x[i:j], 10 )
		return (n, j + 1)

	elif b'0'[0] <= x[i] and x[i] <= b'9'[0]:
		j = x.index( b':', i )
		n = int( x[i:j], 10 )
		j += 1
		return (x[j:j+n], j + n)

	elif x[i] == b'n'[0]:
		return (None, i + 1)

	elif x[i] == b'l'[0]:
		i += 1
		r = []
		while x[i] != b'e'[0]:
			(v, i) = decode( x, i, decode )
			r.append( v )
		return (r, i + 1)

	elif x[i] == b'd'[0]:
		i += 1
		r = {}
		while x[i] != b'e'[0]:
			(k   , i) = decode( x, i, decode )
			(r[k], i) = decode( x, i, decode )
		return (r, i + 1)

	else:
		raise ValueError()


def decode( x, i = 0, decode = _decode ):
	return _decode( x, i, decode )


def _encode( x, encode ):
	if isinstance( x, int ):
		return b'i' + str( int( x ) ).encode() + b'e'

	elif isinstance( x, bytes ) or isinstance( x, bytearray ):
		return str( len( x ) ).encode() + b':' + x

	elif x is None:
		return b'n'

	elif isinstance( x, collections.Mapping ):
		pairs = sorted( x.items() )
		content = b''.join(
			encode( k, encode ) + encode( v, encode )
			for k, v in pairs
		)
		return b'd' + content + b'e'

	elif isinstance( x, collections.Iterable ):
		content = b''.join( encode( i, encode ) for i in x )
		return b'l' + content + b'e'

	else:
		raise ValueError()


def encode( x, encode = _encode ):
	return _encode( x, encode )
