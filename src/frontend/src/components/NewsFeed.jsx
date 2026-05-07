import React, { useState, useEffect } from 'react';
import axios from 'axios';

function NewsFeed() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await axios.get('/api/news');
        setNews(response.data);
      } catch (error) {
        console.error("Error fetching news:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchNews();
  }, []);

  if (loading) return <p>Đang tải tin tức...</p>;
  if (news.length === 0) return <p>Chưa có tin tức nào. Vui lòng bấm Cập nhật DL.</p>;

  return (
    <div>
      <h2>Tiến bộ AI mới nhất</h2>
      <div className="grid-container">
        {news.map((item) => (
          <div key={item.id} className="glass-card">
            <h3>{item.title}</h3>
            <p style={{ marginBottom: '1rem', fontSize: '0.9rem' }}>
              {new Date(item.published_at).toLocaleDateString()}
            </p>
            <p>{item.summary}</p>
            {item.url && (
              <a 
                href={item.url} 
                target="_blank" 
                rel="noopener noreferrer"
                style={{ display: 'inline-block', marginTop: '1rem', color: 'var(--accent-color)', textDecoration: 'none' }}
              >
                Đọc thêm &rarr;
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default NewsFeed;
