# airklassmissions

<br>

## ✅ 프로젝트 개요
- **큐리어슬리 에어클래스 서비스 개발과제를 진행합니다.**
- 에어클래스 서비스처럼 강사가 강의를 생성하고 유저는 모든 강의에 질문 생성 및 삭제가 가능합니다. 
- 답변이 달린 질문은 삭제가 불가능하며 강사는 자신이 생성한 모든 강의에 달린 질문에 답변을 남길 수 있습니다. 강사 역시 작성된 질문을 삭제할 수 있습니다.
- 모든 사용자는 특정 강의에 작성된 질문과 답변을 확인할 수 있습니다.

<br>

📖 **Contents**

- [사용 기술](#사용-기술)
- [이슈 관리](#이슈-관리)
- [코드 컨벤션](#코드-컨벤션)
- [API 명세서](#api-명세서)
- [ERD](#erd)
- [커밋 컨벤션](#커밋-컨벤션)
- [브랜치 전략](#브랜치-전략)
- [주석 처리](#주석-처리)
- [Test Case](#test-case)
- [실행 가능한 방법](#실행-가능한-방법)
- [과제를 진행하면서 특별히 신경 쓴 부분](#과제를-진행하면서-특별히-신경-쓴-부분)


<br>

## 사용 기술
- API 서버<br>
![python badge](https://img.shields.io/badge/Python-3.9-%233776AB?&logo=python&logoColor=white)
![django badge](https://img.shields.io/badge/Django-3.1.14-%23092E20?&logo=Django&logoColor=white)
![DRF badge](https://img.shields.io/badge/DRF-3.13.1-%23092E20?&logo=DRF&logoColor=white)
![DRFsimpleJWT badge](https://img.shields.io/badge/DRFsimpleJWT-%23092E20?&logo=DRF&logoColor=white)

- DB<br>
![SQLite badge](https://img.shields.io/badge/SQLite-%23092E20?&logo=SQLite&logoColor=white)

- ETC<br>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white"/>
  
<br>

## 이슈 관리
<img width="1163" alt="image" src="https://user-images.githubusercontent.com/95380638/192075374-08435671-9828-4e3c-aaa5-69239024595e.png">

**수행해야 할 개발 사항을 github 칸반보드를 이용해 태스크 및 일정관리를 진행했습니다.** <br>

<br>

## 코드 컨벤션

**Formatter**
- isort
- black

<img width="672" alt="image" src="https://user-images.githubusercontent.com/95380638/192086048-78520675-9660-4e96-9295-b49ad043b553.png">


**로컬에서 pre-commit 라이브러리를 사용해서 git commit 전에 isort와 black를 한번에 실행하여 코드 컨벤션을 준수합니다. 만약 통과되지 않는다면 커밋이 불가능하게 설정합니다.**

<br>

- **클래스와 모델 정의 : PascalCase(파스칼 케이스)**
  - 첫 문자를 모두 대문자로 표기

- **변수와 함수명 정의 : snake_case(스네이크 케이스)**
  - 띄어쓰기를 언더바를 통해 구분해서 표기

<br>

## API 명세서
<img width="1045" alt="image" src="https://user-images.githubusercontent.com/95380638/192076360-cd13a4b7-20e9-4a47-b0c6-ded968ffb067.png">

- **`POST` /api/v1/users/signup** : 누구나 회원가입을 진행할 수 있게 하는 API입니다. is_master 필드를 false로 설정 후 JSON 형태로 요청하면 수강생으로 가입이 진행되고, true로 설정 후 요청하면 강사로 가입이 진행됩니다.
- **`POST` /api/v1/users/signin** : 로그인을 진행하는 API입니다. DRFsimpleJWT 라이브러리를 설치해서 JWT 인증을 진행했습니다. 로그인 성공 시, 클라이언트에게 access token과 refresh token을 리턴합니다.
- **`POST` /api/v1/token/refresh** : access token이 만료되는 경우, 해당 API로 access token 및 refresh token 재발급할 수 있게 설정했습니다. settings.py에서 SIMPLE_JWT의 설정 중, ROTATE_REFRESH_TOKENS이라는 항목을 True로 설정하여 재발급 시, access token만 갱신되는 것이 아니라 refresh token도 같이 갱신되도록 진행합니다.
- **`POST` /api/v1/klasses** : 로그인된 강사만 요청이 가능하고 강의를 생성하는 API입니다. 
  - 강사만 요청을 할 수 있도록 djangomission - permissions.py에 IsOwner 클래스를 정의했습니다. has_permission 메서드로 로그인이 된 유저가 master 객체를 가지고 있을 때만 인증을 진행했습니다. 
- **`GET` /api/v1/klasses/<klass_id>** : 특정 강의에 작성된 질문과 답변을 확인할 수 있는 API입니다. 서비스에 로그인한 모든 유저가 요청 가능합니다. 
- **`POST` /api/v1/klasses/<klass_id>/questions** : 특정 강의에 속하는 질문을 생성할 수 있는 API입니다. 서비스에 로그인한 모든 유저가 요청 가능합니다.
- **`PATCH` /api/v1/questions/<question_id>** : 유저가 생성한 질문을 삭제 및 복구하거나, 강사가 생성한 강의에 달린 질문을 삭제 및 복구할 수 있습니다. 서비스에 로그인한 모든 유저가 요청 가능하지만, 유저의 경우 답변이 달린 질문은 삭제가 불가능합니다. 강사로 로그인한 경우, 강사가 생성한 강의에 대해서만 질문을 삭제/복구할 수 있습니다.
  - Question 모델의 is_deleted 필드를 사용해서 DB에 데이터를 완전히 삭제하는 것이 아닌 soft delete를 진행했습니다. 추후에 다시 복구하는 경우에는 편리하다고 판단했습니다.
- **`POST` /api/v1/questions/<question_id>/answer** : 강사가 생성한 강의에 달린 질문에 답변을 생성하는 API입니다. 로그인된 강사만 요청이 가능합니다.

<br>

<summary>🚀 API 호출 테스트 결과</summary>
<div markdown="1">
<ul>
  <li>
    <p>회원가입</p>
    <img width="778" alt="image" src="https://user-images.githubusercontent.com/95380638/192079005-89eca546-34b2-4ebd-946b-5ab995f86d4e.png">
  </li>
  <li>
    <p>로그인</p>
    <img width="772" alt="image" src="https://user-images.githubusercontent.com/95380638/192079030-b4ba4e58-a189-42c2-8190-42a920da78e6.png">
  </li>
  <li>
    <p>access token 및 refresh token 재발급</p>
    <img width="787" alt="image" src="https://user-images.githubusercontent.com/95380638/192079051-eee62ab0-224f-4b77-b4c9-1ed2aefdcc5d.png">
  </li>
  <li>
    <p>강사가 강의 생성</p>
    <img width="785" alt="image" src="https://user-images.githubusercontent.com/95380638/192079106-56676afd-d474-4962-8e71-1f5d9952c20b.png">
  </li>
  <li>
    <p>특정 강의에 작성된 질문과 답변 확인</p>
    <img width="782" alt="image" src="https://user-images.githubusercontent.com/95380638/192079162-0dff47d7-fdb5-4909-90e0-2ca95a846cc8.png">
    <img width="788" alt="image" src="https://user-images.githubusercontent.com/95380638/192079177-0b9b4daa-2730-4364-a076-96cf4c08d5d9.png">
  </li>
  <li>
    <p>유저가 특정 강의에 속하는 질문 생성</p>
    <img width="789" alt="image" src="https://user-images.githubusercontent.com/95380638/192079281-0c2a291e-f579-469a-9fef-4bc4962046e2.png">
  </li>
  <li>
    <p>유저가 생성한 질문 삭제 및 복구 / 강사가 생성한 강의에 달린 질문 삭제 및 복구</p>
    <img width="780" alt="image" src="https://user-images.githubusercontent.com/95380638/192079317-17734975-fac5-4e09-aeca-24f9d35d3e90.png">
    <img width="781" alt="image" src="https://user-images.githubusercontent.com/95380638/192079338-7c5d2f5d-38a9-4f1e-bd15-799a95340d20.png">
    <p>유저가 질문 삭제 및 복구</p>
    <img width="781" alt="image" src="https://user-images.githubusercontent.com/95380638/192079371-6b3514bf-4b47-4073-92e8-70ca64679720.png">
    <p>유저가 질문 삭제 시, 답변이 있는 경우</p>
    <img width="795" alt="image" src="https://user-images.githubusercontent.com/95380638/192079386-5676a4cb-6c22-43f2-8547-4652ed1c5f86.png">
    <img width="793" alt="image" src="https://user-images.githubusercontent.com/95380638/192079390-aa7fad17-6f6d-4c45-8689-853f08c9154b.png">
    <p>강사가 질문 삭제 시, 본인이 생성하지 않은 강의의 경우와 본인이 생성한 강의일 경우</p>
    <br>
  </li>
  <li>
    <p>강사가 생성한 강의에 달린 질문에 답변 생성</p>
    <img width="800" alt="image" src="https://user-images.githubusercontent.com/95380638/192079483-edcce517-e711-47e9-8366-61de227d30cc.png">
    <img width="791" alt="image" src="https://user-images.githubusercontent.com/95380638/192079496-1578732d-bb32-4075-a2b0-5cb7fe045a52.png">
    <p>강사가 생성한 강의에 달린 질문에 답변을 생성하고 해당 강의 조회</p>
  </li>

</ul>
</div>


<br>

## ERD
<img width="1045" alt="image" src="https://user-images.githubusercontent.com/95380638/192076755-875a83eb-8864-43d9-8466-750a78fd53ec.png">

<br>

- User 모델과 Master 모델을 1:1 관계로 설정했습니다. 1명의 유저는 is_master 필드값에 따라 에어클래스 서비스의 유저(수강생) 또는 강사로 등록될 수 있습니다.
  - django Signal을 이용하여 User 모델 생성 시, is_master 필드값이 True라면 Master 모델 객체를 생성하게끔 설정했습니다.
- User 모델과 Question 모델을 1:N 관계로 설정했습니다. 1명의 유저는 여러 개의 질문을 생성할 수 있습니다.
- Klass 모델과 Question 모델을 1:N 관계로 설정했습니다. 1개의 강의는 여러 개의 질문이 달릴 수 있습니다.
- Master 모델과 Klass 모델을 1:N 관계로 설정했습니다. 1명의 강사는 여러 개의 강의를 생성할 수 있습니다.
- Master 모델과 Answer 모델을 1:N 관계로 설정했습니다. 1명의 강사는 자신이 생성한 여러 개의 질문에 대한 여러 개의 답변을 작성할 수 있습니다.
- Question 모델과 Answer 모델을 1:1 관계로 설정했습니다. 1개의 질문에는 1개의 답변이 달릴 수 있습니다. 

<br>

## 커밋 컨벤션
```terminal
# --- 제목(title) ---
# <타입(type)> <#이슈 번호> <제목(title)>
# 예시(ex) : Docs(Add) #14 Readme 수정

# --- 본문(content) ---
# 예시(ex) :
# - Workflow
# - 커밋 메시지에 대한 문서 제작 추가.
# - commit message docs add.

# --- COMMIT END ---
# <타입> 리스트
#   init    : 초기화
#   feat    : 기능추가
#   add     : 내용추가
#   update  : 기능 보완 (업그레이드)
#   fix     : 버그 수정
#   refactor: 리팩토링
#   style   : 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없음)
#   docs    : 문서 (문서 추가(Add), 수정, 삭제)
#   test    : 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없음)
#   chore   : 기타 변경사항 (빌드 스크립트 수정 등)
# ------------------
#     제목 첫 글자를 대문자로
#     제목 끝에 마침표(.) 금지
#     본문은 "어떻게" 보다 "무엇을", "왜"를 설명한다.
# ------------------
```

<br>

## 브랜치 전략
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/95380638/192081927-df671fec-f568-442a-a9ab-3a9d7d35b43c.png">

- **main** : 최종적으로 문제가 없고 완전히 개발된 기능을 포함하는 브랜치
- **feature** : issue에 부여한 기능을 개발하는 브랜치로 기능 개발이 완료되면 main 브랜치에 Merge 진행

<br>

## 주석 처리
```python
# url : GET /api/v1/klasses/<klass_id>
class KlassRetrieveAPIView(APIView):
    """
    Assignee : 상백

    permission = 서비스에 로그인한 모든 유저가 요청 가능
    Http method = GET
    GET : 특정 강의에 작성된 질문과 답변 조회
    """
    
    permission_classes = [IsAuthenticated]

    def get(self, request, klass_id):
        """
        Assignee : 상백

        특정 강의를 조회하기 위한 메서드입니다. 특정 강의의 id값을 path 파라미터로 입력해야 합니다.
        klass_id로 존재하는 객체가 없다면 에러 메시지를 응답합니다.
        """
    ...
```
- **View 클래스** 하단에 해당 코드에 대한 설명을 여러 줄 주석으로 기재
  - 한 줄 주석으로 클래스 위에 URL 기재
- **메소드**별로 하단에 해당 코드에 대한 설명을 여러 줄 주석으로 기재

<br>

## Test Case
<img width="963" alt="image" src="https://user-images.githubusercontent.com/95380638/192100770-6dc6fc85-eca1-4547-87df-44d3c777e4b8.png">

- **총 20개 테스트 진행 완료**
  - `pytest` 및 `pytest-django` 설치 후, 터미널에서 pytest를 입력해서 테스트 진행 완료
  - `DRF의 APIClient 및 APITestCase`로 테스트 코드 작성

- **테스트 진행 내용**
  - `accounts_tests` : 회원가입 테스트, 회원 로그인 테스트 진행
  - `contentshub_tests` : 로그인된 강사의 강의 생성 테스트, 로그인된 유저의 강의 생성 테스트 진행 
  - `community_tests` 
      - 로그인된 유저가 특정 강의에 작성된 질문과 답변을 확인하는 테스트, 로그인된 유저가 존재하지 않는 강의에 작성된 질문과 답변을 확인하는 테스트 진행
      - 로그인된 유저가 특정 강의에 속하는 질문을 생성하는 테스트, 로그인된 유저가 특정 강의에 적합하지 않은 필드 데이터를 입력해 질문을 생성하는 테스트, 로그인된 유저가 존재하지 않는 강의에 속하는 질문을 생성하는 테스트 진행
      - 로그인된 유저가 생성한 질문을 삭제 및 복구하는 테스트, 로그인된 유저가 변경할 수 없는 필드 데이터를 입력하면서 질문을 삭제 및 복구하는 테스트, 로그인된 유저가 존재하지 않는 질문을 삭제 및 복구하는 테스트, 로그인된 유저가 답변이 있는 질문을 삭제하려고 하는 테스트, 로그인된 강사가 생성한 질문을 삭제 및 복구하는 테스트, 로그인된 강사가 생성하지 않은 질문을 삭제 및 복구하는 테스트 진행
      - 로그인된 강사가 생성한 강의에 달린 질문에 답변을 생성하는 테스트, 로그인된 강사가 생성하지 않은 강의의 질문에 답변을 생성하는 테스트 진행

<br>

## 실행 가능한 방법
- 에어클래스 서비스 과제를 진행하면서 `pipenv` 라는 패키지 관리 도구를 사용했습니다. 

<br>

### 로컬 환경 설정 방법
- 먼저 `git clone https://github.com/tkdqor/airklassmissions.git` 해당 명령어로 clone를 진행합니다. <br>
- 그리고 `djangomission` 프로젝트 루트 디렉터리 위치에 `Pipfile 파일`과 `Pipfile.lock 파일`이 있는지 확인한 후 `pipenv install` 명령어를 입력해주면 됩니다.
- 이후에는 제가 메일로 전달해드린 my_settings.py를 `djangomission` 프로젝트 루트 디렉터리 위치에 넣고 `settings.py의 SECRET_KEY`를 적용시킵니다. (프로젝트 진행시에는 my_settings.py라는 파일을 .gitignore에 설정했었습니다.)
- 그리고 `pipenv shell` 명령어로 가상환경을 활성화합니다.
- 마지막으로 `python manage.py runserver`로 서버를 실행하고 `python manage.py migrate` 명령어로 migrate를 진행합니다.

<br>

- 만약, 위의 과정을 진행해도 로컬 서버가 구현이 되지 않는다면 `pip install pipenv` 명령어로 pip를 이용해 pipenv를 설치하고 다시 진행할 수 있습니다.
- 만약, 특정 라이브러리를 설치하라는 에러 메세지가 출력된다면 `pipenv install 라이브러리 이름` 명령어로 설치를 진행할 수 있습니다. ex) `pipenv install Django==3.1.14`
- 위의 과정을 자세하게 담은 블로그는 [다음](https://www.daleseo.com/python-pipenv/)과 같습니다.
- 만약, pipenv의 과정이 진행되지 않을 경우를 대비해 프로젝트 루트 디렉토리에 requirements.txt를 생성해서 commit를 진행했습니다. `pip install --upgrade pip` 명령어 이후, `pip install -r requirements.txt` 명령어로 진행할 수 있습니다.

<br>

### Postman 테스트 진행 과정
- `DRFsimpleJWT` 라이브러리를 설치해서 JWT 인증을 진행했습니다. 
- `POST` /api/v1/users/signin 해당 API로 로그인이 성공되면 access token을 응답받을 수 있습니다.
<img width="775" alt="image" src="https://user-images.githubusercontent.com/95380638/192087402-a719b1c2-3be2-4af7-a74c-ddd825b07b88.png">

- 다른 API 요청 시, `Auth - Type - OAuth 2.0`을 선택 후, 위에서 확인한 access token를 입력하고 요청을 진행할 수 있습니다.
<img width="792" alt="image" src="https://user-images.githubusercontent.com/95380638/192087454-1a95b93c-ff57-4b2a-beeb-9d20a673e02b.png">



<br>

## 과제를 진행하면서 특별히 신경 쓴 부분
- **API 요청별로 예외처리 및 200, 201, 400, 404 status code를 나눠서 API 응답 로직을 구성했습니다.**
  - 더 Restful한 API 응답을 진행하기 위해 `status code`를 구분했습니다.
  - 객체가 존재하지 않는 `DoesNotExist` 에러가 발생하는 경우, 예외처리를 진행하여 에러가 발생한 이유를 메세지로 작성했습니다.

- **Soft delete를 구현했습니다.**
  - `PATCH` /api/v1/questions/<question_id>로 API 요청을 하는 경우, 유저가 생성한 질문을 삭제 및 복구하거나 강사가 생성한 강의에 달린 질문을 삭제 및 복구를 진행합니다.
  - 이 때, DB에 저장된 데이터를 완전히 삭제하는 것이 아니라 Question 모델의 is_deleted 필드를 BooleanField로 설정하고 default는 False / API 요청 시 True로 값을 변경해서 특정 강의에 작성된 질문과 답변을 확인할 때는 filter(is_deleted=False) 이렇게 ORM 메서드로 응답을 진행했습니다.
  - 바탕화면의 `휴지통`과 같이 유저나 강사가 삭제한 질문들을 다시 복구하는 경우를 고려해봤습니다. 
  - 또한, 하나의 API로 삭제 및 복구를 구현하는 점은, reqeust가 요청되었을 때 결과가 언제나 같아야 하는 `멱등성`의 개념에도 `PATCH` method는 구현 방법에 따라 멱등성이 보장되거나 아닐 수 있다는 점에서 문제가 없다고 판단하여 진행했습니다.

- **django signal를 통해 자동으로 Master 모델의 객체 데이터를 생성했습니다.**
  - 어떤 특정한 일이나 이벤트를 수행할 때마다 그 때 지정한 동작을 수행할 수 있게 해주는 `django signal`를 이용하여 User 모델 생성 시, is_master 필드값이 True라면 Master 모델 객체를 자동으로 생성할 수 있게 구현했습니다.
  - User 모델에서 is_master 필드로도 에어클래스 서비스를 이용하는 수강생과 강사를 구분할 수 있으나, 과제에서 Master 모델을 구현하라고 명시했고 Master 모델을 구현하는 것이 추후에 강사별 강의 목록 API나 강사와 관련된 유의미한 데이터를 관리하는데 있어 꼭 필요하다고 판단했습니다.

- **pre-commit을 적용하여 코드 컨벤션 및 commit 컨벤션을 지키려 노력했습니다.**
  - `pre-commit` 라이브러리란, commit 메세지를 작성하기 전에 호출을 해서 .pre-commit-config.yaml 파일에 설정한 formatter나 linter를 적용하여 코드 컨벤션을 지켜나갈 수 있게 해줍니다.
  - 에어클래스 서비스 과제에서는 `isort`와 `black`이라는 formatter를 적용했습니다.
  - 또한, 미리 정해놓은 commit 컨벤션을 따라서 commit를 진행했습니다.
  - **`이렇게 저는 만약 회사에 입사하게 되면, 회사의 정해진 컨벤션들을 가장 우선적으로 습득해서 개발 업무를 진행하고 소통하는 데 있어 문제가 없도록 노력하는 개발자가 되고 싶습니다.`**

