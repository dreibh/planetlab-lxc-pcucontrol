//-------------------------------------------------------------------
//   Copyright (C) The Internet Society (1999).  All Rights Reserved.
//
//   This document and translations of it may be copied and furnished to
//   others, and derivative works that comment on or otherwise explain it
//   or assist in its implementation may be prepared, copied, published
//   and distributed, in whole or in part, without restriction of any
//   kind, provided that the above copyright notice and this paragraph are
//   included on all such copies and derivative works.  However, this
//   document itself may not be modified in any way, such as by removing
//   the copyright notice or references to the Internet Society or other
//   Internet organizations, except as needed for the purpose of
//   developing Internet standards in which case the procedures for
//   copyrights defined in the Internet Standards process must be
//   followed, or as required to translate it into languages other than
//   English.
//
//   The limited permissions granted above are perpetual and will not be
//   revoked by the Internet Society or its successors or assigns.
//
//   This document and the information contained herein is provided on an
//   "AS IS" basis and THE INTERNET SOCIETY AND THE INTERNET ENGINEERING
//   TASK FORCE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING
//   BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION
//   HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF
//   MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
//   
//   
//   Modifiyed by Intel Corporation, 2005
//-------------------------------------------------------------------------

#define HASHLEN 16
typedef unsigned char HASH[HASHLEN];
#define HASHHEXLEN 32
typedef char HASHHEX[HASHHEXLEN+1];

/* calculate H(A1) as per HTTP Digest spec */
void DigestCalcHA1(
    char * pszAlg,
    char * pszUserName,
    char * pszRealm,
    char * pszPassword,
    char * pszNonce,
    char * pszCNonce,
    HASHHEX SessionKey
    );

/* calculate request-digest/response-digest as per HTTP Digest spec */
void DigestCalcResponse(
    HASHHEX HA1,           /* H(A1) */
    char * pszNonce,       /* nonce from server */
    char * pszNonceCount,  /* 8 hex digits */
    char * pszCNonce,      /* client nonce */
    char * pszQop,         /* qop-value: "", "auth", "auth-int" */
    char * pszMethod,      /* method from the request */
    char * pszDigestUri,   /* requested URL */
    HASHHEX HEntity,       /* H(entity body) if qop="auth-int" */
    HASHHEX Response      /* request-digest or response-digest */
    );

