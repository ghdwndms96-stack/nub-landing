# 눕 NUB · NFC 랜딩페이지

NFC 키링을 태그하면 열리는 페이지예요. 소개글, 캐릭터 영상, 응원 메시지 소통창이 들어 있어요.

## 폴더 구성

| 위치 | 내용 |
|---|---|
| `landing/templates/landing/index.html` | 페이지 본문 (글, 캐릭터 정보, 영상 링크) |
| `landing/static/landing/img/` | 캐릭터 이미지 (`nanubo`, `pin`, `gurbang`, `seo`, `bibi`, `mong`, `group` .webp) |
| `landing/models.py` | 응원 메시지 저장 구조 |
| `render.yaml`, `build.sh` | Render 배포 설정 |

## 1. GitHub에 올리기

1. GitHub에서 새 저장소를 만들어요. 이름은 예를 들어 `nub-landing`으로 하고, 이미 만든 `g9`를 써도 돼요.
2. 저장소 화면에서 **Add file → Upload files**를 누르고, 이 폴더 안의 파일과 폴더를 전부 끌어다 놓은 뒤 **Commit changes**를 눌러요.
   - `.gitignore`처럼 점(.)으로 시작하는 파일도 같이 올려 주세요.

## 2. Render에 배포하기

1. [render.com](https://render.com)에 GitHub 계정으로 로그인해요.
2. **New → Blueprint**를 누르고 방금 만든 저장소를 고르면, `render.yaml`을 읽어서 웹 서버와 데이터베이스를 함께 만들어요.
3. 중간에 입력칸이 나오면 관리자 계정 정보를 넣어요.
   - `DJANGO_SUPERUSER_USERNAME`: 관리자 아이디 (예: `juni`)
   - `DJANGO_SUPERUSER_PASSWORD`: 비밀번호 (길고 어렵게)
   - `DJANGO_SUPERUSER_EMAIL`: 이메일
4. **Apply**를 누르고 몇 분 기다리면 `https://nub-landing.onrender.com` 같은 주소가 생겨요.

> **무료 요금제 주의**
> - 웹 서버는 한동안 접속이 없으면 잠들어서, 첫 접속 때 열리기까지 시간이 걸려요.
> - 무료 데이터베이스는 일정 기간이 지나면 만료되니, Render 화면의 안내를 꼭 확인하세요.
> - 실제 손님을 받기 시작하면 둘 다 유료 플랜으로 올리는 걸 추천해요.

## 3. 응원 메시지 관리하기

- `https://내주소/admin/`에 들어가서 위에서 정한 아이디로 로그인해요.
- **응원 메시지** 목록에서 부적절한 글은 **숨김**에 체크하면 페이지에서 사라져요. 지우지 않아서 기록은 남아요.
- 같은 사람이 20초 안에 연달아 글을 쓰지 못하게 막혀 있어요.

## 4. 영상 넣기

1. 영상을 유튜브에 **일부 공개**로 올려요.
2. `landing/templates/landing/index.html`에서 각 친구 줄의 `yt:""` 따옴표 안에 링크를 붙여 넣어요.
   ```
   {id:"pin",name:"핀", ... yt:"https://youtu.be/영상아이디", ...
   ```
3. GitHub에서 파일을 고쳐 저장하면 Render가 자동으로 다시 배포해요.

## 5. NFC 태그에 주소 쓰기

'NFC Tools' 같은 앱으로 친구별 주소를 써요. 그러면 태그하자마자 그 친구가 맨 위에 나오고, 영상과 응원창도 그 친구로 맞춰져요.

| 친구 | 주소 끝에 붙이는 것 |
|---|---|
| 나눕오 | `/#nanubo` |
| 핀 | `/#pin` |
| 구르방 | `/#gurbang` |
| 세오 | `/#seo` |
| 비비 | `/#bibi` |
| 몽이 | `/#mong` |

예: `https://nub-landing.onrender.com/#pin`

## 6. 내 도메인 연결하기 (추천)

NFC 태그는 한 번 쓰면 바꾸기 번거로우니, 태그에 쓰기 **전에** 내 도메인을 연결하는 게 좋아요.

1. Render 서비스 → **Settings → Custom Domains**에서 도메인을 추가하고, 안내대로 도메인 업체의 DNS를 설정해요.
2. **Environment**에 `EXTRA_HOSTS`를 추가하고 값에 `nub.kr,www.nub.kr`처럼 도메인을 넣어요.

## 이미지 바꾸기

`landing/static/landing/img/` 안의 파일을 **같은 이름**(`pin.webp` 등)으로 바꿔 올리면 돼요. PNG를 쓰고 싶으면 파일 이름은 그대로 두고 확장자만 다르게 올린 뒤 알려 주세요. 코드에서 확장자를 바꿔야 해요.

## 내 컴퓨터에서 미리 보기 (선택)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
DEBUG=1 python manage.py runserver
```
`http://127.0.0.1:8000`에서 열려요.
