/*
 *Progcessed By JSDec in 0.07s
 *JSDec - JSDec.js.org
 */
var I1lli1 = function () {
  var _0x212228 = true;
  return function (_0xf378bd, _0x453f56) {
    var _0x402ad5 = _0x212228 ? function () {
      if (_0x453f56) {
        var _0x5d8b94 = _0x453f56["apply"](_0xf378bd, arguments);

        _0x453f56 = null;
        return _0x5d8b94;
      }
    } : function () {};

    _0x212228 = false;
    return _0x402ad5;
  };
}();

var lillIi = I1lli1(this, function () {
  var _0xe0483d = function () {
    return "dev";
  },
      _0x23a7eb = function () {
    return "window";
  };

  var _0x7ae092 = function () {
    var _0x35c4b9 = new RegExp("\\w+ *\\(\\) *{\\w+ *['|\"].+['|\"];? *}");

    return !_0x35c4b9["test"](_0xe0483d["toString"]());
  };

  var _0x25b675 = function () {
    var _0x55400e = new RegExp("(\\\\[x|u](\\w){2,4})+");

    return _0x55400e["test"](_0x23a7eb["toString"]());
  };

  var _0x56c077 = function (_0x14fc4f) {
    var _0x3001ff = 0;

    if (_0x14fc4f["indexOf"](false)) {
      _0x4aac8(_0x14fc4f);
    }
  };

  var _0x4aac8 = function (_0x36f234) {
    var _0x2338df = 3;

    if (_0x36f234["indexOf"]("true"[3]) !== _0x2338df) {
      // _0x56c077(_0x36f234);
    }
  };

  if (!_0x7ae092()) {
    if (!_0x25b675()) {
      _0x56c077("ind\u0435xOf");
    } else {
      _0x56c077("indexOf");
    }
  } else {
    _0x56c077("ind\u0435xOf");
  }
});
lillIi();
var hexcase = 0;
var b64pad = "";
var chrsz = 8;

function hex_sha1(lIIii1) {
  return binb2hex(core_sha1(str2binb(lIIii1), lIIii1["length"] * chrsz));
}

function b64_sha1(lili1) {
  return binb2b64(core_sha1(str2binb(lili1), lili1["length"] * chrsz));
}

function core_sha1(liliI, ll1lI) {
  liliI[ll1lI >> 5] |= 128 << 24 - ll1lI % 32;
  liliI[(ll1lI + 64 >> 9 << 4) + 15] = ll1lI;
  var ii1I11 = Array(80);
  var liIi1 = 1732584193;
  var lI11II = -271733879;
  var l1llI1 = -1732584194;
  var llIIll = 271733878;
  var IillIi = -1009589776;

  for (var lii = 0; lii < liliI["length"]; lii += 16) {
    var liIl1 = liIi1;
    var llliil = lI11II;
    var II1lll = l1llI1;
    var II1lli = llIIll;
    var ii1I1I = IillIi;

    for (var lil = 0; lil < 80; lil++) {
      if (lil < 16) {
        ii1I11[lil] = liliI[lii + lil];
      } else {
        ii1I11[lil] = rol(ii1I11[lil - 3] ^ ii1I11[lil - 8] ^ ii1I11[lil - 14] ^ ii1I11[lil - 16], 1);
      }

      var IillIl = safe_add(safe_add(rol(liIi1, 5), sha1_ft(lil, lI11II, l1llI1, llIIll)), safe_add(safe_add(IillIi, ii1I11[lil]), sha1_kt(lil)));
      IillIi = llIIll;
      llIIll = l1llI1;
      l1llI1 = rol(lI11II, 30);
      lI11II = liIi1;
      liIi1 = IillIl;
    }

    liIi1 = safe_add(liIi1, liIl1);
    lI11II = safe_add(lI11II, llliil);
    l1llI1 = safe_add(l1llI1, II1lll);
    llIIll = safe_add(llIIll, II1lli);
    IillIi = safe_add(IillIi, ii1I1I);
  }

  return Array(liIi1, lI11II, l1llI1, llIIll, IillIi);
}

function sha1_ft(IiIi, iI1ll1, IlI1Il, l1il1l) {
  if (IiIi < 20) {
    return iI1ll1 & IlI1Il | ~iI1ll1 & l1il1l;
  }

  if (IiIi < 40) {
    return iI1ll1 ^ IlI1Il ^ l1il1l;
  }

  if (IiIi < 60) {
    return iI1ll1 & IlI1Il | iI1ll1 & l1il1l | IlI1Il & l1il1l;
  }

  return iI1ll1 ^ IlI1Il ^ l1il1l;
}

function sha1_kt(i11I11) {
  return i11I11 < 20 ? 1518500249 : i11I11 < 40 ? 1859775393 : i11I11 < 60 ? -1894007588 : -899497514;
}

function safe_add(iIII1I, ilil1i) {
  var lI1liI = (iIII1I & 65535) + (ilil1i & 65535);
  var i1i1Ii = (iIII1I >> 16) + (ilil1i >> 16) + (lI1liI >> 16);
  return i1i1Ii << 16 | lI1liI & 65535;
}

function rol(lllii, iI11Ii) {
  return lllii << iI11Ii | lllii >>> 32 - iI11Ii;
}

function str2binb(il1i11) {
  var iil1ii = Array();
  var IlIlli = 255;

  for (var il1i1i = 0; il1i1i < il1i11["length"] * chrsz; il1i1i += chrsz) {
    iil1ii[il1i1i >> 5] |= (il1i11["charCodeAt"](il1i1i / chrsz) & IlIlli) << 24 - il1i1i % 32;
  }

  return iil1ii;
}

function binb2hex(iil1ll) {
  var lI1lll = "0123456789abcdef";
  var iIiII = "";

  for (var iil1lI = 0; iil1lI < iil1ll["length"] * 4; iil1lI++) {
    iIiII += lI1lll["charAt"](iil1ll[iil1lI >> 2] >> (3 - iil1lI % 4) * 8 + 4 & 15) + lI1lll["charAt"](iil1ll[iil1lI >> 2] >> (3 - iil1lI % 4) * 8 & 15);
  }

  return iIiII;
}

function binb2b64(iiiliI) {
  var IIIII1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  var I1lIlI = "";

  for (var ii1ill = 0; ii1ill < iiiliI["length"] * 4; ii1ill += 3) {
    var II1iI = (iiiliI[ii1ill >> 2] >> 8 * (3 - ii1ill % 4) & 255) << 16 | (iiiliI[ii1ill + 1 >> 2] >> 8 * (3 - (ii1ill + 1) % 4) & 255) << 8 | iiiliI[ii1ill + 2 >> 2] >> 8 * (3 - (ii1ill + 2) % 4) & 255;

    for (var llI1II = 0; llI1II < 4; llI1II++) {
      if (ii1ill * 8 + llI1II * 6 > iiiliI["length"] * 32) {
        I1lIlI += b64pad;
      } else {
        I1lIlI += IIIII1["charAt"](II1iI >> 6 * (3 - llI1II) & 63);
      }
    }
  }

  return I1lIlI;
}


var Base64 = {

    // private property
    _keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    // public method for encoding
    , encode: function (input)
    {
        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;

        input = Base64._utf8_encode(input);

        while (i < input.length)
        {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);

            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;

            if (isNaN(chr2))
            {
                enc3 = enc4 = 64;
            }
            else if (isNaN(chr3))
            {
                enc4 = 64;
            }

            output = output +
                this._keyStr.charAt(enc1) + this._keyStr.charAt(enc2) +
                this._keyStr.charAt(enc3) + this._keyStr.charAt(enc4);
        } // Whend

        return output;
    } // End Function encode


    // public method for decoding
    ,decode: function (input)
    {
        var output = "";
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;

        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
        while (i < input.length)
        {
            enc1 = this._keyStr.indexOf(input.charAt(i++));
            enc2 = this._keyStr.indexOf(input.charAt(i++));
            enc3 = this._keyStr.indexOf(input.charAt(i++));
            enc4 = this._keyStr.indexOf(input.charAt(i++));

            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;

            output = output + String.fromCharCode(chr1);

            if (enc3 != 64)
            {
                output = output + String.fromCharCode(chr2);
            }

            if (enc4 != 64)
            {
                output = output + String.fromCharCode(chr3);
            }

        } // Whend

        output = Base64._utf8_decode(output);

        return output;
    } // End Function decode


    // private method for UTF-8 encoding
    ,_utf8_encode: function (string)
    {
        var utftext = "";
        string = String(string).replace(/\r\n/g, "\n");

        for (var n = 0; n < string.length; n++)
        {
            var c = string.charCodeAt(n);

            if (c < 128)
            {
                utftext += String.fromCharCode(c);
            }
            else if ((c > 127) && (c < 2048))
            {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            }
            else
            {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }

        } // Next n

        return utftext;
    } // End Function _utf8_encode
    // private method for UTF-8 decoding
    ,_utf8_decode: function (utftext)
    {
        var string = "";
        var i = 0;
        var c, c1, c2, c3;
        c = c1 = c2 = 0;

        while (i < utftext.length)
        {
            c = utftext.charCodeAt(i);

            if (c < 128)
            {
                string += String.fromCharCode(c);
                i++;
            }
            else if ((c > 191) && (c < 224))
            {
                c2 = utftext.charCodeAt(i + 1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            }
            else
            {
                c2 = utftext.charCodeAt(i + 1);
                c3 = utftext.charCodeAt(i + 2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }

        } // Whend

        return string;
    } // End Function _utf8_decode

};


window = {
    'localStorage': {
        'setItem': setItem,
        'getItem': getItem,
    },
    'btoa': btoa,
};

function setItem(key, val) {
    window[key] = val;
    window['localStorage'][key] = val;
};

function getItem(key) {
    return window[key]
};

function btoa(val) {
    s = Base64.encode(val);
    return s
};

function get_token() {
    a = String(Date.parse(new Date()) / 1000);
    window.localStorage.setItem('token', window.btoa(a)+('|')+binb2b64(hex_sha1(window.btoa(core_sha1(a)))) + b64_sha1(a));
    return window.localStorage.token
};

console.log(get_token());

// MTYwODEwNjg2OA==|AAAAAgAAAAIAAAAAAAAAAAAAAAkAAAAJAAAAAQAAAAAAAAAIAAAABgAAAAAAAAAHAAAACAAAAAMAAAAIAAAAAAAAAAAAAAAIAAAABgAAAAAAAAACAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAkAAAAIAAAABAAAAAkAAAAFAAAAAAAAAAkAAAAFAAAAAwAAAAAAAAAAAAAABQptE49FrFXsJo+ecEVIpFMVX7/zo

// MTYwODEwNjg2OA==|AAAAAgAAAAcAAAABAAAACQAAAAAAAAAAAAAABAAAAAAAAAAHAAAAAAAAAAAAAAAAAAAACAAAAAcAAAAJAAAABgAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAIAAAAAAAAAAgAAAAgAAAAAAAAAAAAAAAYAAAAAAAAACQAAAAAAAAAHAAAABwAAAAAAAAAGAAAAAAAAAAAAAAAIAAAAAAptE49FrFXsJo+ecEVIpFMVX7/zo

