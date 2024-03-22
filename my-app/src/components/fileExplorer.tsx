import React, { useEffect, useState } from 'react';
import { S3 } from 'aws-sdk';

// Define TypeScript types for the component props
interface FileExplorerProps {
  bucketName: string;
}

// Define TypeScript type for the file objects we'll be working with
interface S3Object {
  Key: string;
  LastModified: Date;
}

const FileExplorer: React.FC<FileExplorerProps> = ({ bucketName }) => {
  const [files, setFiles] = useState<S3Object[]>([]);

  useEffect(() => {
    const fetchFiles = async () => {
      const s3 = new S3({
        region: 'us-west-2',
        credentials: {
          accessKeyId: 'ASIAYZ3ZDWWLEJHK2N64',
          secretAccessKey: '+IBzSNbMdzwWF+TeJFsmIRUBaJNbyQcrFt7stH20',
        },
      });

      try {
        const response = await s3.listObjectsV2({ Bucket: bucketName }).promise();
        const objects: S3Object[] = response.Contents?.map(obj => ({
          Key: obj.Key!,
          LastModified: obj.LastModified!,
        })) ?? [];
        setFiles(objects);
      } catch (error) {
        console.error("Error fetching files from S3:", error);
      }
    };

    fetchFiles();
  }, [bucketName]);

  return (
    <div>
      <ul>
        {files.map(file => (
          <li key={file.Key}>
            {file.Key} - Last Modified: {file.LastModified.toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FileExplorer;
