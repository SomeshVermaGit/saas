'use client';

import { useState } from 'react';
import BackendStatus from '@/components/BackendStatus';
import { API_URL } from '@/lib/api';

export default function Home() {
  const [showStatus, setShowStatus] = useState(true);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      {/* Header */}
      <header className="border-b bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-xl">AI</span>
              </div>
              <div>
                <h1 className="text-xl font-bold">AI Knowledge Assistant</h1>
                <p className="text-xs text-gray-600 dark:text-gray-400">Powered by FastAPI + Next.js</p>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <a
                href="/dashboard"
                className="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors"
              >
                Dashboard
              </a>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-16">
          <h2 className="text-5xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            AI-Powered Knowledge Workflows
          </h2>
          <p className="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
            Transform your documents into intelligent workflows with AI assistance
          </p>
        </div>

        {/* Backend Connection Status */}
        <div className="flex justify-center mb-16">
          {showStatus ? (
            <BackendStatus />
          ) : (
            <button
              onClick={() => setShowStatus(true)}
              className="text-sm text-blue-600 hover:underline"
            >
              Show Backend Status
            </button>
          )}
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          <FeatureCard
            icon="📄"
            title="Document Management"
            description="Upload and organize your documents with AI-powered processing"
            endpoint="/api/documents"
          />
          <FeatureCard
            icon="💬"
            title="AI Chat"
            description="Chat with your documents using advanced AI models"
            endpoint="/api/chat"
          />
          <FeatureCard
            icon="⚡"
            title="Workflows"
            description="Automate your knowledge workflows with custom pipelines"
            endpoint="/api/workflows"
          />
          <FeatureCard
            icon="👥"
            title="User Management"
            description="Secure authentication and user profile management"
            endpoint="/api/auth"
          />
        </div>

        {/* API Information */}
        <div className="bg-white dark:bg-gray-800 rounded-xl p-8 border shadow-sm">
          <h3 className="text-2xl font-bold mb-4">🔗 API Connection</h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-900 rounded-lg">
              <span className="text-sm font-medium">Backend URL:</span>
              <code className="text-sm text-blue-600 dark:text-blue-400">{API_URL}</code>
            </div>
            <div className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-900 rounded-lg">
              <span className="text-sm font-medium">API Documentation:</span>
              <a
                href={`${API_URL}/docs`}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-blue-600 hover:underline"
              >
                Open Swagger Docs →
              </a>
            </div>
            <div className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-900 rounded-lg">
              <span className="text-sm font-medium">Health Check:</span>
              <a
                href={`${API_URL}/health`}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-blue-600 hover:underline"
              >
                {API_URL}/health →
              </a>
            </div>
          </div>
        </div>

        {/* Tech Stack */}
        <div className="mt-16 text-center">
          <h3 className="text-lg font-semibold mb-6 text-gray-600 dark:text-gray-400">
            Built with modern technologies
          </h3>
          <div className="flex flex-wrap justify-center gap-4">
            <TechBadge>Next.js 15</TechBadge>
            <TechBadge>FastAPI</TechBadge>
            <TechBadge>PostgreSQL</TechBadge>
            <TechBadge>MongoDB</TechBadge>
            <TechBadge>Redis</TechBadge>
            <TechBadge>OpenAI</TechBadge>
            <TechBadge>Vercel</TechBadge>
            <TechBadge>Railway</TechBadge>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center text-sm text-gray-600 dark:text-gray-400">
            <p>© 2025 AI Knowledge Assistant. Deployed on Vercel + Railway.</p>
            <p className="mt-2">
              <a href="https://github.com" className="hover:underline">GitHub</a>
              {' · '}
              <a href={`${API_URL}/docs`} className="hover:underline">API Docs</a>
              {' · '}
              <a href="/dashboard" className="hover:underline">Dashboard</a>
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

function FeatureCard({ icon, title, description, endpoint }: {
  icon: string;
  title: string;
  description: string;
  endpoint: string;
}) {
  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-xl border shadow-sm hover:shadow-md transition-shadow">
      <div className="text-4xl mb-3">{icon}</div>
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <p className="text-sm text-gray-600 dark:text-gray-400 mb-3">{description}</p>
      <code className="text-xs text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20 px-2 py-1 rounded">
        {endpoint}
      </code>
    </div>
  );
}

function TechBadge({ children }: { children: React.ReactNode }) {
  return (
    <span className="px-4 py-2 bg-white dark:bg-gray-800 border rounded-full text-sm font-medium shadow-sm">
      {children}
    </span>
  );
}
