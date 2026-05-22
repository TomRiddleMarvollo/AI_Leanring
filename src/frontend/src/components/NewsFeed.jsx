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
    <div className="list-container">
      <h2>Tiến bộ AI mới nhất</h2>
      <div>
        {news.map((item) => (
          <div key={item.id} className="news-item">
            <div className="news-thumbnail">AI NEWS</div>
            <div className="news-content">
              <a href={item.url || '#'} target="_blank" rel="noopener noreferrer" className="news-title">
                {item.title}
              </a>
              <p className="news-summary">{item.summary}</p>
              <div className="news-meta">
                <span className="badge">AI Tech</span>
                <span className="star-rating">
                  {'★'.repeat(item.rating || 0)}{'☆'.repeat(10 - (item.rating || 0))} 
                  <span style={{ color: '#9ca3af', letterSpacing: 'normal', marginLeft: '4px' }}>({item.rating || 0}/10)</span>
                </span>
                <span>{new Date(item.published_at).toLocaleDateString()}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default NewsFeed;
