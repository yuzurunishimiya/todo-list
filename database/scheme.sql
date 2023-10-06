CREATE TABLE IF NOT EXISTS Statuses (
    id SERIAL PRIMARY KEY,
    status VARCHAR(32) NOT NULL,
    code VARCHAR(12) NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
)

CREATE TABLE IF NOT EXISTS Priorities (
    id SERIAL PRIMARY KEY,
    priority VARCHAR(32) NOT NULL,
    code VARCHAR(12) NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
)


CREATE TABLE IF NOT EXISTS Tasks (
    id SERIAL PRIMARY KEY,
    task Varchar(256) NOT NULL,
    status_id INT REFERENCES Statuses(id) ON DELETE RESTRICT NOT NULL,
    priority_id INT REFERENCES Priorities(id) ON DELETE SET NULL,
    start_date_time TIMESTAMPTZ,
    end_date_time TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
)
