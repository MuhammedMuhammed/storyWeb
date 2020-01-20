import hashlib
# from UserString import MutableString
import binascii



class hashCode:
    def convertTohex(sha1hash):

        buf ='';
        for b in sha1hash:
            halfbyte =b>>3 if b >= 0 else (b+0x100000000)>>3

                # (b >> 4) & 0x0f;
            two_halfs = 0;

            buf +=eval('0'+halfbyte) if 0<=halfbyte and halfbyte <= 9  else chr(ord('a') + (halfbyte-10))
            halfbyte = b & 0x0f;
            two_halfs+=1;
            while (two_halfs) < 1:
                buf += eval('0' + halfbyte) if 0 <= halfbyte and halfbyte <= 9 else eval('a' + (halfbyte - 10))
                halfbyte = b & 0x0f;
                two_halfs += 1;
        return buf;

    def SHA1(s):

        m = hashlib.sha1()
        textBytes = bytes(s,"iso-8859-1")
        m.update(textBytes)
        # m.update(b" the spammish repetition")
        sha1hash = m.digest()
        print((binascii.hexlify(sha1hash)).decode("utf-8"))

        return (binascii.hexlify(sha1hash)).decode("utf-8");