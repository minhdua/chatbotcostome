# Chat Bot Hỗ Trợ Tư Vấn Trang Phục

## Giới thiệu

Dự án này nhằm xây dựng một chat bot hỗ trợ tư vấn trang phục và tìm kiếm trang phục theo ảnh cho cửa hàng trang phục. Chat bot sẽ sử dụng ngôn ngữ tiếng Việt để hiểu và trả lời các câu hỏi từ người dùng về các sản phẩm trang phục hiện có trong cửa hàng.

## Yêu cầu

1. Chức năng hỗ trợ tư vấn trang phục dạng text:

- Chat bot có khả năng tư vấn về các loại trang phục mà cửa hàng đang kinh doanh.
- Tư vấn về trang phục mà nhiều người quan tâm.
- Cung cấp thông tin về đặc trưng của trang phục như màu sắc, phong cách, giới tính, v.v.
- Hiển thị giá trang phục khi được yêu cầu.
- Tư vấn theo câu hỏi hoặc theo ngữ cảnh (ý niệm trước đó) từ người dùng.

2. Chức năng hỗ trợ tìm kiếm trang phục theo ảnh (clothes retrieval):

- Người dùng có thể gửi ảnh trang phục lên hệ thống thông qua chat bot.
- Chat bot sẽ trả lời với các sản phẩm tương tự đang có kinh doanh dựa trên ảnh gửi lên.
- Nếu không có sản phẩm tương tự, chat bot sẽ thông báo cho người dùng.

3. Xây dựng Cơ sở dữ liệu sản phẩm của khách hàng:

- Xây dựng và quản lý cơ sở dữ liệu chứa thông tin về các sản phẩm của cửa hàng để cung cấp dữ liệu cho chat bot.

## Giải pháp

- Xây dựng một chatbot webapp đơn giản để cung cấp giao diện cho người dùng cuối.
- Sử dụng các kỹ thuật xử lý ngôn ngữ tự nhiên để hiểu và phân tích ý niệm của người dùng (cho tiếng Việt).
- Thu thập dữ liệu và huấn luyện mô hình chat bot đơn giản để xử lý dữ liệu dạng text và tư vấn trang phục.
- Huấn luyện mô hình trích xuất đặc trưng cho ảnh và sử dụng mô hình này để tìm kiếm các sản phẩm trang phục tương tự dựa trên ảnh được gửi lên.
- Thiết kế cơ sở dữ liệu, thực hiện kết nối và thao tác ghi và truy xuất dữ liệu. Dữ liệu huấn luyện và dữ liệu đã được trích xuất từ mô hình sẽ được lưu trữ trong CSDL.

## Phạm vi

- Dự án tập trung xây dựng chat bot và các chức năng liên quan. Không bao gồm xây dựng toàn bộ hệ thống của cửa hàng trang phục.
- Đội phát triển sẽ chỉ thực hiện việc coding và phát triển project, không tham gia viết bài luận, báo cáo hay kịch bản demo.

## Giao nộp

- Source code của dự án.
- Hướng dẫn sử dụng (guideline).
- Tài liệu tổng hợp quá trình phát triển.

## Thời gian dự kiến

Dự án dự kiến kéo dài trong 1.5 tháng, bắt đầu từ ngày 23/07/2023. Thời gian này không bao gồm thời gian nghiên cứu và hỗ trợ chạy dự án.

## Hướng phát triển

- [Try on clothes](https://github.com/search?q=deepfashion&type=repositories)
