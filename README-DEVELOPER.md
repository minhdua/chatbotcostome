## Cài đặt Python và Virtual Environment

1. Truy cập trang chủ của Python để tải về phiên bản Python mới nhất: https://www.python.org/downloads/
2. Tải và cài đặt Python theo hướng dẫn trên màn hình.
3. Mở terminal hoặc cmd và kiểm tra phiên bản của Python đã được cài đặt bằng cách chạy lệnh sau:

```bash
python --version
```

4. Cài đặt Virtual Environment bằng cách chạy lệnh sau:

```bash
pip install virtualenv
```

5. Tạo môi trường ảo bằng cách chạy lệnh sau:

```bash
virtualenv venv
```

6. Kích hoạt môi trường ảo bằng lệnh sau:

```bash
source venv/bin/activate
```

hoặc

```bash
source venv/Scripts/activate
```

## Cài đặt các package trong requirements.txt

1. Clone project từ Gitlab

```bash
git clone https://gitlab.com/chatbot-support/chatbotsupportcostume.git
cd chatbotsupportcostume
```

2. Chạy lệnh sau để cài đặt các package có trong file requirements.txt:

```bash
pip install -r requirements.txt
```

3. Download nltk data:

```bash
python -c "import nltk; nltk.download('punkt')"
```

4. Train model:

```bash
python train.py
```

5. Start the Flask app:
   Để chạy ứng dụng trong môi trường Development, hãy sử dụng các lệnh sau:

```bash
export FLASK_ENV=Development
export FLASK_APP=backend/app.py
flask run
```

Để chạy ứng dụng trong môi trường Production, hãy sử dụng các lệnh sau:

```bash
export FLASK_ENV=Production
export FLASK_APP=backend/app.py
flask run
```

Nếu bạn muốn start project giống như Dockerfile, bạn có thể sử dụng lệnh sau để tạo image và chạy container:

```bash
docker build -t chatbot-support-costume .
docker run -p 5000:5000 chatbot-support-costume
```

Sau khi container chạy, bạn có thể truy cập chatbot tại địa chỉ http://localhost:5000.

## Hướng dẫn sử dụng Flask-Migrate cho Flask App

1. Cài đặt Flask-Migrate và SQLAlchemy

Trước tiên, cài đặt Flask-Migrate và SQLAlchemy nếu bạn chưa có chúng:

```bash
pip install Flask-Migrate SQLAlchemy
```

2. Khởi tạo Flask-Migrate
   Sau khi đã cài đặt Flask-Migrate, bạn cần khởi tạo Flask-Migrate:

```bash
flask db init
```

Lệnh này sẽ tạo thư mục migrations, trong đó chứa các file cấu hình và các script migration.

4. Tạo migration
   Để tạo migration, bạn cần chạy lệnh sau:

```bash
flask db migrate -m "create user table"
```

5. Chạy migration
   Để chạy migration, bạn cần chạy lệnh sau:

```bash
flask db upgrade
```

7. Rollback migration
   Để rollback migration, bạn cần chạy lệnh sau:

```bash
flask db downgrade
```

### Hướng dẫn loại bỏ các import không sử dụng và sắp xếp chúng

1.  Cài đặt các công cụ
    Đầu tiên, bạn cần cài đặt `isort` và `autoflake`. Chạy các lệnh sau trong terminal:

```bash
pip install isort autoflake
```

2. Loại bỏ các import không sử dụng
   Bạn có thể sử dụng autoflake để tự động loại bỏ các import không sử dụng từ mã nguồn của bạn. Chạy lệnh sau:

```bash
autoflake --in-place --remove-all-unused-imports your_file.py

```

Hãy thay thế your_file.py bằng tên tập tin chứa mã nguồn của bạn. 3. Sắp xếp lại import
Tiếp theo, sử dụng isort để sắp xếp các import sao cho phù hợp với các hướng dẫn PEP8. Chạy lệnh sau:

```bash
isort your_file.py

```

Câu lệnh này sẽ sắp xếp lại các import theo đúng hướng dẫn PEP8.

Sau khi thực hiện các bước này, mã nguồn của bạn sẽ không còn các import không sử dụng và các import cũng sẽ được sắp xếp một cách ngăn nắp hơn.

### Cài đặt các extension Visual Studio Code cần thiết

1. Mở Visual Studio Code
2. Truy cập vào Extensions Marketplace bằng cách nhấp vào biểu tượng "Extensions" ở thanh bên trái của VS Code
3. Tìm kiếm và cài đặt các extension sau:

- Python
- Docker
- REST Client
  Sau khi cài đặt xong các extension trên, chúng ta có thể phát triển và triển khai dự án ChatbotSupportCostume.

### Huấn luyện model trên Google Colab

1. Truy cập vào đường dẫn sau để mở file notebook trên Google Colab:

(chatbot_support_costume.ipynb)[https://colab.research.google.com/drive/1wwn5xnsLF55grRJ5m64rVf4pc1lBM7pI#scrollTo=JsbpWVssm52m]

### Các tập tin bash và chức hướng

#### pull_code.sh

Tập tin **pull_code.sh** được sử dụng để thực hiện việc kéo mã nguồn mới nhất từ kho lưu trữ từ xa (origin) và cập nhật nhánh hiện tại.

```bash
bash pull_code.sh
```

#### merge_code.sh

Tập tin **merge_code.sh** thực hiện việc pull mã nguồn từ nhánh develop và merge vào nhánh hiện tại.

Hướng dẫn sử dụng:

```bash
merge_code.sh
```

#### push_develop.sh

Tập tin **push_develop.sh** thực hiện việc merge mã nguồn từ nhánh hiện tại vào nhánh develop và sau đó push lên kho lưu trữ từ xa (origin).

Hướng dẫn sử dụng:

```bash
push_develop.sh "Commit message của bạn"
```

#### Lưu ý

Trước khi sử dụng các tập tin bash, hãy chắc chắn đã thay đổi đường dẫn đến thư mục của repository và các tên nhánh theo đúng yêu cầu của dự án.
Các tập tin bash phải được cấp quyền thực thi. Nếu chưa có, bạn có thể thực hiện lệnh sau để cấp quyền:

#### Chạy tập tin run_backend.sh bằng lệnh sau:

```
bash run_backend.sh
```

#### Swagger

Để truy cập vào Swagger UI, bạn có thể truy cập vào đường dẫn sau:

```bash
http://localhost:5000/swagger
```

#### Flask Admin UI

Để truy cập vào Flask Admin UI, bạn có thể truy cập vào đường dẫn sau:

```bash
http://localhost:5000/admin
```
