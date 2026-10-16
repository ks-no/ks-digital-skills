# OAuth2, OpenID Connect, Maskinporten and ID-porten

Load this file when the code gets, validates or uses OAuth2 or OpenID Connect
tokens, or talks to Maskinporten or ID-porten. The facts below come from the
protocol pages of Digdir (docs.digdir.no). If a fact matters for the answer and you
cannot check the current page, add a `Check:` line.

## Validate each incoming token

Use the JWT validation of the framework, and set these values:

- **Signature** with keys from the JWKS endpoint of the issuer. Cache the keys, and
  fetch them again when a token has an unknown `kid`.
- **Algorithm** from a fixed list, for example `RS256`. Never accept `none`, and
  never let the token choose between a public key and a shared secret.
- **`iss`** equal to the issuer that you expect.
- **`aud`** equal to your API or client.
- **`exp`** and **`nbf`**, with a small clock skew.
- **Scope or role** that the endpoint needs.

## Log in users (authorization code flow)

- Use the authorization code flow with PKCE (`S256`). ID-porten requires PKCE for
  public clients.
- Check `state`, and check `nonce` in the ID token.
- Register exact redirect URIs. Do not allow wildcards.
- Keep tokens on the server when you can (a backend for the frontend). Do not put
  tokens in `localStorage`.

## Maskinporten (JWT grant)

The client signs a JWT and sends it to the token endpoint of Maskinporten. The
current values:

| Part | Value |
| --- | --- |
| `alg` | `RS256`, `RS384` or `RS512` |
| `x5c` or `kid` | One of them must be present. `x5c` holds the virksomhetssertifikat (the Norwegian business certificate) and its chain. `kid` names a key that is registered for the client. |
| `aud` | The issuer of Maskinporten: `https://maskinporten.no/` in production, `https://test.maskinporten.no/` in test |
| `iss` | The client ID |
| `scope` | The scopes, separated by spaces |
| `iat` | Now. Maskinporten refuses a value more than 10 seconds in the future. |
| `exp` | At most 180 seconds after `iat`. Digdir recommends 120 seconds. |
| `jti` | A new unique value for each grant. Maskinporten does not accept the same grant twice. |

- Keep the private key or the certificate in a secret store or a key vault. Read the
  path and the password from configuration, not from code.
- Cache the access token until shortly before it expires. Use one cache for the
  process, and let only one call fetch a new token at a time.
- Do not log the grant, the access token or the key.

## ID-porten (OpenID Connect)

- Validate the ID token as OpenID Connect Core 3.1.7 says.
- Check that `acr` is high enough for the service. The values are
  `idporten-loa-substantial`, `idporten-loa-high`, `eidas-loa-substantial`,
  `eidas-loa-high` and `selfregistered-email`.
- Do not check `amr`. Its values can change.
- `pid` is the fødselsnummer or D-number of the user. It is personal data. Do not log
  it, and do not use it as a public ID.
- `sub` is a pairwise ID. It is stable for your client only.
