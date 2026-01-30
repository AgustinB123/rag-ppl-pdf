/*
DROP TABLE [dbo].[PPLSYNC];
DROP TABLE [dbo].[PPLSYNC_CHANGES];
*/

CREATE TABLE [dbo].[PPLSYNC] (
    [Id]         INT          NOT NULL IDENTITY,
	[Usuario]    CHAR (10)    NOT NULL,
	[Fecha]      DATETIME     NOT NULL,
    [Commit]     CHAR (40),
    [Status]     TINYINT
    PRIMARY KEY CLUSTERED ([Id] ASC)
);
CREATE TABLE [dbo].[PPLSYNC_CHANGES] (
    [IdSync]        INT          NOT NULL,
	[ScriptType]    TINYINT      NOT NULL,
	[ScriptId]      CHAR(10)     NOT NULL,
	[ChangeType]    TINYINT      NOT NULL,
    [DbHashHeader] CHAR (40),
	[LocalHashHeader] CHAR (40),
	[DbHashScript] CHAR (40),
	[LocalHashScript] CHAR (40),
    [Status]        TINYINT
);