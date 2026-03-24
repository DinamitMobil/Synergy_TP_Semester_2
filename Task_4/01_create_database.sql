USE master;
GO

IF DB_ID(N'SupportDeskDB') IS NULL
  CREATE DATABASE SupportDeskDB;
GO

USE SupportDeskDB;
GO

IF OBJECT_ID(N'dbo.Tickets', N'U') IS NOT NULL
  DROP TABLE dbo.Tickets;
GO

CREATE TABLE dbo.Tickets (
    TicketID     INT IDENTITY(1,1) PRIMARY KEY,
    ClientName   NVARCHAR(120) NOT NULL,
    Email        NVARCHAR(120) NOT NULL,
    Subject      NVARCHAR(200) NOT NULL,
    Description  NVARCHAR(MAX) NOT NULL,
    Status       NVARCHAR(30) NOT NULL CONSTRAINT DF_Tickets_Status DEFAULT (N'New'),
    CreatedAt    DATETIME2 NOT NULL CONSTRAINT DF_Tickets_CreatedAt DEFAULT (SYSDATETIME())
);
GO

INSERT INTO dbo.Tickets (ClientName, Email, Subject, Description, Status)
VALUES
(N'Иван Петров', N'ivan@example.com', N'Не работает VPN', N'После обновления Windows клиент VPN не подключается.', N'New'),
(N'Мария Смирнова', N'maria@example.com', N'Сброс пароля', N'Нужен доступ к корпоративному порталу.', N'In progress');
GO
