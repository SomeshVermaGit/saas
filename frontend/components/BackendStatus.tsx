'use client';

import { useEffect, useState } from 'react';
import { api, API_URL } from '@/lib/api';

export default function BackendStatus() {
  const [status, setStatus] = useState<'checking' | 'connected' | 'error'>('checking');
  const [message, setMessage] = useState('Checking backend connection...');
  const [version, setVersion] = useState('');

  useEffect(() => {
    checkBackend();
  }, []);

  const checkBackend = async () => {
    setStatus('checking');
    setMessage('Connecting to backend...');

    const result = await api.healthCheck();

    if (result.data) {
      setStatus('connected');
      setMessage('Backend connected successfully!');
      setVersion(result.data.version);
    } else {
      setStatus('error');
      setMessage(result.error || 'Failed to connect to backend');
    }
  };

  return (
    <div className="w-full max-w-md p-4 rounded-lg border">
      <div className="flex items-center justify-between mb-2">
        <h3 className="font-semibold">Backend Status</h3>
        <div className={`w-3 h-3 rounded-full ${
          status === 'connected' ? 'bg-green-500' :
          status === 'error' ? 'bg-red-500' :
          'bg-yellow-500 animate-pulse'
        }`} />
      </div>

      <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">{message}</p>

      {version && (
        <p className="text-xs text-gray-500">Version: {version}</p>
      )}

      <div className="mt-3 text-xs text-gray-500">
        <p className="truncate">API: {API_URL}</p>
      </div>

      {status === 'error' && (
        <button
          onClick={checkBackend}
          className="mt-3 w-full px-3 py-1.5 text-sm bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
        >
          Retry Connection
        </button>
      )}
    </div>
  );
}
