USE quiz_app

-- Drop a table called 'users' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('[dbo].[users]', 'U') IS NOT NULL
DROP TABLE [dbo].[users]
GO