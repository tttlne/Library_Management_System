# Phần mềm quản lí thư viện.
>
> Thành viên nhóm 222:
>
> **Phạm Đăng Phong 22022614**
>
> **Thái Thị Thùy Linh 22022631**
>
> **Thái Nguyễn Hoàng Bách 22022672**
>
> **Phạm Thành Nam 22022618**
>
### Mục lục
[I. Mục đích](#Muc) 

[II . Personas](#Personas)

[III. Scenario](#Scenario)

[IV. User Story](#User)

[V. Tính năng](#T)

[VI. Cách cài đặt và chạy](#C)

[VII. Báo cáo](#B)

<a name = "Muc"></a>
# Mục đích
Một hệ thống quản lí thư viện được phát triển bằng Python. Nó bao gồm các tính năng như: Quản lý tài liệu, tìm kiếm và tra cứu, quản lí người dùng, quản lí mượn trả và một số tính năng khác nhằm nâng cao hiệu quả hoạt động của thư viện, cải thiện trải nghiệm của người dùng, và hỗ trợ ban quản lý thư viện trong việc điều hành và phát triển dịch vụ.

<a name = "Personas"></a>
# Personas
**Tên**: Nguyễn Thị Mai

**Tuổi**: 35

**Chức vụ**: Thủ thư chính

- **Mục tiêu**: Quản lý sách và tài liệu hiệu quả, đảm bảo việc mượn và trả sách diễn ra suôn sẻ, cập nhật và duy trì cơ sở dữ liệu thư viện chính xác, hỗ trợ người dùng tìm kiếm thông tin và tài liệu.

- **Nhu cầu**: Mai cần một phần mềm để giúp cô ấy quản lý thư viện dễ dàng với giao diện quản lý dễ sử dụng và trực quan, có chức năng tìm kiếm mạnh mẽ và nhanh chóng và báo cáo chi tiết về số lượng sách, tình trạng sách.

<a name = "Scenario"></a>
# Scenario
- **Bối cảnh**: Nguyễn Thị Mai, thủ thư chính, đang quản lý việc mượn và trả sách hàng ngày tại thư viện. Một ngày, cô phải xử lý một số lượng lớn sách trả lại và muốn đảm bảo rằng tất cả các sách được cập nhật trạng thái chính xác trong hệ thống.

- **Hành động**:

1. Nguyễn Thị Mai đăng nhập vào phần mềm quản lý thư viện bằng tài khoản của mình.
2. Cô chọn chức năng "Quản lý mượn/trả sách".
3. Cô quét mã vạch hoặc sử dụng RFID để cập nhật thông tin sách trả lại.
4. Hệ thống tự động cập nhật trạng thái sách từ "Đang mượn" thành "Có sẵn".
5. Cô kiểm tra danh sách sách trả lại để đảm bảo tất cả đã được cập nhật.

- **Kết quả mong muốn**:
Nguyễn Thị Mai hoàn thành việc cập nhật trạng thái sách một cách nhanh chóng và chính xác, giảm thiểu lỗi và tăng hiệu quả công việc. Cô có thể dễ dàng kiểm tra và xác nhận tình trạng sách.
<a name = "User"></a>
# User Story
- **Người dùng**: nguyễn Thị Mai

**Là một** thủ thư

**Tôi muốn** quét mã vạch hoặc sử dụng RFID để cập nhật thông tin sách mượn và trả,

**Để** tôi có thể quản lý tình trạng sách nhanh chóng và chính xác

<a name = "T"></a>
# Tính năng
- Thêm sách vào thư viện
- Xóa sách khỏi thư viện
- Cập nhật trạng thái sách (mượn/trả)
- Xem danh sách sách có trong thư viện

<a name = "C"></a>
# Cách cài đặt và chạy
tạo 1 data base db gồm 3 table
+--------------+
| Tables_in_db |
+--------------+
| books        |
| books_issued |
| users        |
+--------------+

CREATE TABLE books (
    bid VARCHAR(10) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE books_issued (
    bid VARCHAR(10) NOT NULL,
    issuedto VARCHAR(255) NOT NULL,
    PRIMARY KEY (bid)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
<a name = "B"></a>
# Báo cáo



