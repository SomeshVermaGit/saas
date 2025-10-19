// API Client for Backend Communication
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface ApiResponse<T> {
  data?: T;
  error?: string;
}

class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  private async request<T>(
    endpoint: string,
    options?: RequestInit
  ): Promise<ApiResponse<T>> {
    try {
      const response = await fetch(`${this.baseUrl}${endpoint}`, {
        ...options,
        headers: {
          'Content-Type': 'application/json',
          ...options?.headers,
        },
      });

      if (!response.ok) {
        const error = await response.text();
        return { error: error || `HTTP ${response.status}` };
      }

      const data = await response.json();
      return { data };
    } catch (error) {
      return {
        error: error instanceof Error ? error.message : 'Network error'
      };
    }
  }

  // Health Check
  async healthCheck() {
    return this.request<{ status: string; version: string }>('/health');
  }

  // Auth endpoints
  async login(email: string, password: string) {
    return this.request('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  }

  async register(email: string, password: string, name: string) {
    return this.request('/api/auth/register', {
      method: 'POST',
      body: JSON.stringify({ email, password, name }),
    });
  }

  // Documents endpoints
  async getDocuments(token: string) {
    return this.request('/api/documents', {
      headers: { Authorization: `Bearer ${token}` },
    });
  }

  async uploadDocument(token: string, file: FormData) {
    return this.request('/api/documents/upload', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
      body: file,
    });
  }

  // Chat endpoints
  async sendMessage(token: string, message: string) {
    return this.request('/api/chat', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
      body: JSON.stringify({ message }),
    });
  }

  // Workflows endpoints
  async getWorkflows(token: string) {
    return this.request('/api/workflows', {
      headers: { Authorization: `Bearer ${token}` },
    });
  }
}

export const api = new ApiClient(API_URL);
export { API_URL };
